from django.db import models
from datetime import datetime
import calendar


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
            if f.editable and f.name not in 'id':
                fields.append(
                    {
                        'label': f.verbose_name,
                        'name': f.name,
                        'value': value,
                    }
                )
        return fields

    @classmethod
    def date_is_valide(cls, date_text, format='%d-%m-%Y %H:%M'):
        try:
            if date_text != datetime.strptime(date_text, format).strftime(format):
                raise ValueError
            return True
        except ValueError:
            return False

    @classmethod
    def get_datetimes(cls, dates, dates_datetime, format='%d-%m-%Y %H:%M'):
        dates_datetime = dates_datetime
        result = True
        for key in dates.keys():
            if not cls.date_is_valide(dates[key], format):
                result = False
            else:
                dates_datetime[key] = datetime.strptime(dates[key], format)
        return result

    @classmethod
    def get_first_month_day(cls):
        return datetime.now().replace(day=1, hour=0, minute=0, second=0)

    @classmethod
    def get_last_month_day(cls):
        date_now = datetime.now()
        return date_now.replace(day=calendar.monthrange(date_now.year, date_now.month)[1], hour=23, minute=59, second=59)