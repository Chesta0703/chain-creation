from django.urls import path
from .views import mine_block

urlpatterns = [
    path('mine_block/', mine_block, name='mine_block'),
]
