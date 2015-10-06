from django.dispatch import Signal


grading_event = Signal(providing_args=["module", "grade", "max_grade"])
