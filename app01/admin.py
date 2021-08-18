from django.contrib import admin
from app01.models import DDR, Serdes, U2, U3, Pll, Hdmi, Dp
from app01.models import TVSensor, MIPI, SARADC, VDAC, Package
# ['DDR', 'Serdes', 'U2', 'U3', 'PLL', 'HDMI', 'DP', 'TVSensor',
# 'MIPI', 'SARADC', 'VDAC', 'Package', 'Process Node', 'PPA', '商务']

# Register your models here.
admin.site.register(DDR)
admin.site.register(Serdes)
admin.site.register(U2)
admin.site.register(U3)
admin.site.register(Pll)
admin.site.register(Hdmi)
admin.site.register(Dp)

admin.site.register(TVSensor)
admin.site.register(MIPI)
admin.site.register(SARADC)
admin.site.register(VDAC)
admin.site.register(Package)
