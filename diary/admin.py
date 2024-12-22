from django.contrib import admin
from .models import Page
from .models import Anniversary


# 管理サイトにPage（Modelの）のデータが表示されるようになる
# しかし以下の設定だとidやcreateDateなど編集不可のデータが表示されない
# admin.site.register(Page)

# 以下のように設定するとIDも読み取り専用のフィールドとして設定
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
  readonly_fields=["id", "create_date","update_date"]

@admin.register(Anniversary)
class AnniversaryAdmin(admin.ModelAdmin):
  readonly_fields=["id","access_date"]
