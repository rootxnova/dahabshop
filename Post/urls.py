from django.conf.urls import url
from . import views

app_name = 'Post'

urlpatterns = [
	
	url(r'^$',views.all_categories,name='all_categories'),
	url(r'^clothes$',views.all_clothes,name='all_clothes'),
	url(r'^electronics$',views.all_electronics,name='all_electronics'),
	url(r'^houseware$',views.all_houseware,name='all_houseware'),
	url(r'^(?P<id>\d+)$',views.post,name='post'),
	url(r'^contact',views.contact,name='contact'),
	url(r'^programming$',views.all_programming,name='all_programming'),
	url(r'^social$',views.all_socialmedia,name='all_socialmedia'),
	url(r'^add$',views.add,name='add'),
	url(r'^download$',views.download,name='download'),
	url(r'^statue$',views.statue,name='statue'),
	url(r'^charge$',views.charge,name='charge'),

]