from django.db import models
from pathlib import Path
import uuid

class Page(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
  title = models.CharField(max_length=100, verbose_name="タイトル")
  body = models.TextField(max_length=5000, verbose_name="本文")
  page_date =models.DateField(verbose_name="日付")
  picture=models.ImageField(upload_to="diary/picture/", blank=True, null=True, verbose_name="写真")
  # auto_now_add は該当のデータが初めて作成されたその時の日時を保存
  create_date =models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
  # auto_now は該当データが保存更新されるたびにその時の日時を保存
  update_date =models.DateTimeField(auto_now=True, verbose_name="更新日時")

  def __str__(self):
    return self.title
  
  def oldPictureDelete(self, oldPicture):
    if oldPicture:
      Path(oldPicture.path).unlink(missing_ok=True)
    
  def delete(self, *args, **kwargs):
    picture = self.picture
    print(picture)
    super().delete(*args, **kwargs)
    if picture:
      Path(picture.path).unlink(missing_ok=True)

class Anniversary(models.Model):
  id = models.IntegerField(primary_key=True, editable=False, verbose_name="ID")
  access_date =models.DateTimeField(auto_now_add=True, verbose_name="アクセス日時")
  anniv1=models.CharField(max_length=50, verbose_name="記念日1", null=True)
  anniv2=models.CharField(max_length=50, verbose_name="記念日2", null=True)
  anniv3=models.CharField(max_length=50, verbose_name="記念日3", null=True)
  anniv4=models.CharField(max_length=50, verbose_name="記念日4", null=True)
  anniv5=models.CharField(max_length=50, verbose_name="記念日5", null=True)

  def __str__(self):
    return self.anniv1