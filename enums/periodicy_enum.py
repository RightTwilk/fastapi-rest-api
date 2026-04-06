from enum import Enum

class Periodicity(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"
    BIWEEKLY = "biweekly"      # раз в две недели
    BIMONTHLY = "bimonthly"    # раз в два месяца