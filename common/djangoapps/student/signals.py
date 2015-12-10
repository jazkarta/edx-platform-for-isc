from django.dispatch import Signal


va_enrollment_event = Signal(providing_args=["student", ])
