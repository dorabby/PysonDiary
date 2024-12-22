from django.urls import path
from . import views

app_name="diary"
urlpatterns=[
  # path("どんなパスか", 動かす関数, name="名前")

  # 日記アプリのトップページ
  path("", views.index, name="index"),
  # 日記作成ページ
  path("page/create/", views.page_create, name="page_create"),
  # 日記一覧ページ
  path("pages", views.page_list, name="page_list"),
  # 日記詳細ページ
  path("page/<uuid:id>/", views.page_detail, name="page_detail"),
  # 日記更新ページ
  path("page/<uuid:id>/update/", views.page_update, name="page_update"),
  # 日記削除ページ
  path("page/<uuid:id>/delete/", views.page_delete, name="page_delete"),
  # 今日は何の日検索結果
  path("search/anniversaries", views.search_anniversaries, name="search_anniversaries"),
  # 気象予報確認ページ
  path("check/weather", views.check_weather, name="check_weather")
]