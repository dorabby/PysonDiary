import requests
import pytz
from django.shortcuts import render, redirect,get_object_or_404
import datetime
# ログインを必須にするMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# 汎用的なView用の基底クラス
from django.views import View
from .forms import PageForm
from .models import Page
from .models import Anniversary
# タイムゾーン
from zoneinfo import ZoneInfo
# BeautifulSoupはWebページの情報を取ってくる専門のライブラリ
from bs4 import BeautifulSoup



# トップぺージ
class IndexView(LoginRequiredMixin, View):
  def get(self,request):
    datetime_now=datetime.datetime.now(
      ZoneInfo("Asia/Tokyo")
    ).strftime("%Y年%m月%d日 %H:%M:%S")
    # 画面を返す
    return render(
      request,"diary/index.html", {"datetime_now": datetime_now})

# ページ作成
class PageCreateView(LoginRequiredMixin,View):
  def get(self, request):
    # form=PageForm()はforms.pyで作成したPageFormクラスを呼び出している
    form=PageForm()
    return render(
      request,"diary/page_form.html", {"form": form})
  
  def post(self, request):
    form=PageForm(request.POST, request.FILES) 
    if form.is_valid():
      form.save()
      # 日記の一覧へリダイレクト
      return redirect("diary:page_list")
    # バリデーションチェックに引っかかった場合
    return render(request, "diary/page_form.html", {"form": form})

# 一覧ページ
class PageListView(LoginRequiredMixin,View):
  def get(self, request):
    page_list=Page.objects.order_by("-page_date")#order_byしたい要素の前に-付けると降順になる
    return render(request, "diary/page_list.html", {"page_list": page_list})

# 詳細ページ
class PageDetailView(LoginRequiredMixin,View):
  def get(self, request,id):
    # get_list_or_404一致するIDが無ければ404ページへ
    # (Page,id=id)でPageテーブルのid一致するデータを指定している
    page=get_object_or_404(Page,id=id)
    return render(request, "diary/page_detail.html", {"page":page})

# ページ更新
class PageUpdateView(LoginRequiredMixin,View):
    def get(self, request,id):
      page=get_object_or_404(Page,id=id)
      # (instance=page)登録されていたデータをFormに含める
      form=PageForm(instance=page)
      return render(request, "diary/page_update.html", {"form":form})
    def post(self, request, id):
      page=get_object_or_404(Page,id=id)
      oldPicture=page.picture
      form=PageForm(request.POST, request.FILES, instance=page)
      if form.is_valid():
        # 更新前ファイルがあれば削除処理
        if oldPicture:
          page.oldPictureDelete(oldPicture)
        form.save()
        return redirect("diary:page_detail", id=id)
      return render(request, "diary/page_form.html", {"form": form})

# ページ削除
class PageDeleteView(LoginRequiredMixin,View):
    def get(self, request,id):
      page=get_object_or_404(Page,id=id)
      return render(request, "diary/page_confirm_delete.html", {"page":page})
    
    def post(self,request, id):
      page=get_object_or_404(Page,id=id)
      page.delete()
      return redirect('diary:page_list')

# 記念日取得
class SearchAnnivarsariesView(LoginRequiredMixin,View):
  def get(self,request):
      # 今日の日付を取得
      today = datetime.date.today()
      month = today.month
      day = today.day
      mmdd = today.strftime('%m%d')
      print(today)

      todayAnniv=Anniversary.objects.filter(id=1).first()
      print(todayAnniv)
      if todayAnniv is not None:
        # DBから取得したaccsess_dataのTZをjst形式に変換
        jst = pytz.timezone('Asia/Tokyo')
        utc_time = todayAnniv.access_date  # データベースから取得したUTC時間
        todayAnniv_jst_time = utc_time.astimezone(jst)
        if todayAnniv_jst_time.strftime("%Y-%m-%d") == today.strftime("%Y-%m-%d"):
          # 叩かれた日とDBのaccess_dateが同じ場合、DBから記念日を取得しhtmlへセットする
          result=todayAnniv.anniv1,todayAnniv.anniv2,todayAnniv.anniv3,todayAnniv.anniv4,todayAnniv.anniv5
        else:
          # DBを確認して、保存された日付と違う場合、APIにリクエストする
          # powered by whatistodayAPI
          url = f"https://api.whatistoday.cyou/v3/anniv/" + mmdd
          r = requests.get(url).json()
          # 取得後DBを更新する（何度もAPIを叩かないようにするため）
          result=r["anniv1"],r["anniv2"],r["anniv3"],r["anniv4"],r["anniv5"]
          todayAnniv.access_date= datetime.date.today()
          todayAnniv.anniv1=r["anniv1"]
          todayAnniv.anniv2=r["anniv2"]
          todayAnniv.anniv3=r["anniv3"]
          todayAnniv.anniv4=r["anniv4"]
          todayAnniv.anniv5=r["anniv5"]
          todayAnniv.save()
      else:
          # DBに情報が無い場合APIにリクエストする
          url = f"https://api.k9r06rlu.me/v3/anniv/" + mmdd
          r = requests.get(url).json()
          # 取得後DBを更新する（何度もAPIを叩かないようにするため）
          result=r["anniv1"],r["anniv2"],r["anniv3"],r["anniv4"],r["anniv5"]
          todayAnniv = Anniversary()
          todayAnniv.anniv1=r["anniv1"]
          todayAnniv.anniv2=r["anniv2"]
          todayAnniv.anniv3=r["anniv3"]
          todayAnniv.anniv4=r["anniv4"]
          todayAnniv.anniv5=r["anniv5"]
          todayAnniv.save()
      return render(request, "diary/search_anniversaries.html", {"result_list":result, "month":month, "day":day})

# 明日の天気
class checkWeatherView(LoginRequiredMixin,View):
  def get(self,request):
    # Yahoo天気のurl
    weather_url="https://weather.yahoo.co.jp/weather/jp/27/6200.html"
    # Yahoo天気のweather_urlの情報を取得する
    response=requests.get(weather_url)
    # htmlを見やすいようにparseする
    html=BeautifulSoup(response.text, "html.parser")
    # 以下取得したhtmlの中から必要な情報を取得していく。第一引数にタグ、第二引数に属性を指定できる。
    # 今日明日の天気取得
    forecast=html.find_all("div", attrs={"class":"forecastCity"})[0]
    # 結果用配列用意
    result={}
    # 明日の天気取得
    tomorrow=forecast.find_all("div")[1]
    result['weather']=tomorrow.find_all("p", attrs={"class":"pict"})[0].text.replace("\n","").replace(" ","")
    # 最高最低気温を取得
    result['high']=tomorrow.find_all("li")[0].text
    result['low']=tomorrow.find_all("li")[1].text
    # 降水確率を6時間ごとに取得
    result['rain_06']=tomorrow.find_all("td")[4].text
    result['rain_612']=tomorrow.find_all("td")[5].text
    result['rain_1218']=tomorrow.find_all("td")[6].text
    result['rain_1824']=tomorrow.find_all("td")[7].text

    return render(request, "diary/check_weather.html",{"result":result})

# IndexViewクラスを関数に変換（ここ忘れやすいので忘れない）
index = IndexView.as_view()
page_create= PageCreateView.as_view()
page_list = PageListView.as_view()
page_detail=PageDetailView.as_view()
page_update=PageUpdateView.as_view()
page_delete=PageDeleteView.as_view()
search_anniversaries=SearchAnnivarsariesView.as_view()
check_weather=checkWeatherView.as_view()

