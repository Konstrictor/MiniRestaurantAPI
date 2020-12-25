from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .views import *

router = routers.DefaultRouter()
router.register("produit", ProduitViewset)
router.register("serveur", ServeurViewset)
router.register("table", TableViewset)
router.register("detailstock", DetailStockViewset)
router.register("detail_commande", DetailCommandeViewset)
router.register("paiement", PaiementViewset)
router.register("fournisseur", FournisseurViewset)
router.register("recette", RecetteViewset)
router.register("commande", CommandeViewset)

urlpatterns = [
	path("api/", include(router.urls)),
	path("", include(router.urls)),
	path('api-auth/', include('rest_framework.urls')),
	path('login/', TokenPairView.as_view()),
	path('refresh/', TokenRefreshView.as_view())
]