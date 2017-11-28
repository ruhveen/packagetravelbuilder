from model.package import Package
from model.day_route import DayRoute
from datetime import datetime, timedelta

class PackageBuilder(object):

    @staticmethod
    def build(from_date, to_date, from_budget, to_budget, categories):


        from_budget = int(from_budget)
        to_budget = int(to_budget)
        from_date = datetime.strptime(from_date,'%d-%m-%Y')
        to_date = datetime.strptime(to_date,'%d-%m-%Y')

        days = []

        # Temp patch
        budget = ((to_budget - from_budget) / 2) + from_budget
        total_days = (to_date - from_date).days
        for i in xrange(total_days):
            days.append(PackageBuilder.build_day(from_date + timedelta(days=i), budget /total_days, categories))
        return Package(days=days,total_budget = budget)

    @staticmethod
    def build_day(date, daily_budget, categories):
        d = DayRoute(date=date, budget=daily_budget)
        d.build(categories)
        return d