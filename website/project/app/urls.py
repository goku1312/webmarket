from django.urls import path

from app import views


urlpatterns=[
    path("cadmin",views.cadmin),
path("cadmin1",views.cadmin1),
    path("",views.index,name='index'),
    path("index",views.index),
    path("login",views.login),
    path("k",views.k),
    path("userhome",views.userhome),
    path("registerr",views.registerr),
    path("profile",views.profile),
    # path("payment",views.payment),
    # path("card",views.card),
   path("logout",views.logout),
    #  path("temp_view/<int:template_card_id>/index",views.index),
    #     path("premium_view/<int:template_card_id>/index",views.index,name="card"),

    path("temp_view/<int:template_card_id>/",views.temp_view,name="temp_view"),
        path("premium_view/<int:template_card_id>/",views.premium_view,name="premium_view"),
         path("premium_view/<int:template_card_id>/payment",views.payment,name="payment"),
          path("temp_view/<int:template_card_id>/payment",views.payment,name="payment"),
          path("premium_view/<int:template_card_id>/card",views.card,name="card"),
          path("temp_view/<int:template_card_id>/card",views.card,name="card"),
    path("frame",views.frame),
    path("adminbilling",views.adminbilling),
    path("premiumtemp",views.premiumtemp),
    path("nonpremiumtemp",views.nonpremiumtemp),


]
