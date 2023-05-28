from . import models, choices


class ShowtimeServices:
    def get_price(self, obj):
        """
        Calculates ticket price.
        """
        showtime = models.Showtime.objects.get(id=obj.showtime_id.id)
        price = self.get_status_price(status_name=obj.price_age, showtime_obj=showtime)

        return price

    @staticmethod
    def get_status_price(status_name: str, showtime_obj: models.Showtime):
        if status_name == choices.PriceAges.Adult:
            return showtime_obj.price_adult
        if status_name == choices.PriceAges.Child:
            return showtime_obj.price_child
        if status_name == choices.PriceAges.Student:
            return showtime_obj.price_student
        if status_name == choices.PriceAges.Vip:
            return showtime_obj.price_vip
