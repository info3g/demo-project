from django.contrib import admin

# Register your models here.
from app1.models import Paras,data1,data2,more
admin.site.register(Paras)
admin.site.register(data1)
admin.site.register(data2)
admin.site.register(more)

# {{d1.0.name}}
#     {{d1.1.name}}


# If len(Executors) == 0:
# “I have no executor.”
# If len(Executors) == 1:
# Paras.get(id=id).context =>
# If len(Executors) > 1:
# “The following Executors will be appointed”
# For index, executor in enumerate(Executors):
# If executor.name != ‘moron’
# {index}. {Executor Details}
#
#
# Class Paras(model.Models):
# Para = models.TextField()  ⇒ “{Executor Details} will be appointed.”
