from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def model_to_dict(self):
        data = {}
        for field in self._meta.fields:
            data[field.name] = field.value_from_object(self)
            if isinstance(field, ForeignKey):
                data[field.name] = field.rel.to.objects.get(pk=data[field.name])
        return data

    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_' + fname + '_display'
            if hasattr(self, get_choice):
                value = getattr(self, get_choice)()
            else:
                try:
                    value = getattr(self, fname)
                except AttributeError:
                    value = None

            # only display fields with values and skip some fields entirely
            if f.editable and f.name not in ('id'):
                fields.append(
                    {
                        'label': f.verbose_name,
                        'name': f.name,
                        'value': value,
                    }
                )
        return fields


    def date_validate(date_text, format='%d-%m-%Y %H:%M'):
        try:
            if date_text != datetime.strptime(date_text, format).strftime(format):
                raise ValueError
            return True
        except ValueError:
            return False