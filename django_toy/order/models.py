from django.db import models

# Create your models here.
class Order(models.Model):
    ord_ymd = models.CharField(max_length=16, vebose_name='ORD_YMD')
    acct_mang_dbrn_code = models.CharField(max_length=16, vebose_name='ACCT_MANG_DBRN_CODE')
    ord_no = models.IntegerField(vebose_name='ORD_NO')
    acct_no = models.CharField(max_length=64, vebose_name='ACCT_NO')
    callv_type_code = models.CharField(max_length=32, vebose_name='CALLV_TYPE_CODE')
    sell_buy_tp_code = models.IntegerField(vebose_name='SELL_BUY_TP_CODE')
    stbd_code = models.CharField(max_length=16, vebose_name='STBD_CODE')
    ord_qty = models.IntegerField(vebose_name='ORD_QTY')
    ord_uv = models.IntegerField(vebose_name='ORD_UV')
    mgrn_base_uv = models.IntegerField(vebose_name='MGRN_BASE_UV')

    class Meta:
        db_table = 'shinhan_order'
        verbose_name = '주문정보'
        verbose_name_plural = '주문정보'