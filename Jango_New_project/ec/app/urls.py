from django.urls import path
from . import views
from django.contrib.auth  import views as auth_view,logout
from .forms import LoginForm ,PasswordChangeForm,MyPasswordChangeForm
# from views import password_change,password_change_done



urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact,name='contact'),
    path("category/<slug:val>",views.CategoryVies.as_view(), name='category'),
    path("category-title/<val>",views.CategoryTitle.as_view(), name='category-title'),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(), name='product-detail'),
    path('profile/',views.ProfileView.as_view(), name='profile'),
    path('address/',views.address, name='address'),
    path('updateAddress/<int:pk>/',views.updateAddress.as_view(),name='updateAddress'),
    path('logout/',views.custom_logout,name='logout'),


    # In urls.py

    # path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-cart/',views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart, name = 'showcart'),
    path('checkout/',views.show_cart, name='checkout'),

    path("cart/increment/<int:cart_id>/", views.increment_cart_item, name="increment_cart_item"),
    path("cart/decrement/<int:cart_id>/", views.decrement_cart_item, name="decrement_cart_item"),
    path("cart/remove/<int:cart_id>/", views.remove_from_cart, name="remove_from_cart"),  # Add this line

    # path('cart/increment/<int:cart_id>/', views.increment_cart_item, name='increment_cart_item'),
    # path('cart/decrement/<int:cart_id>/', views.decrement_cart_item, name='decrement_cart_item'),


    # path('add-to-cart/', views.add_to_cart, name='add-to-cart'),  # Add item to cart
    # path('cart/', views.show_cart, name='showcart'),  # View the cart
    # path('checkout/', views.checkout, name='checkout'),  # Checkout page

   


    #Authentication login

    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    # path('login/',views.login_page,name='login'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name="app/login.html",authentication_form=LoginForm,success_url=''),name='login'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name ='app/password_reset.html', form_class = PasswordChangeForm),name='password_reset'),

    # path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone'),name='passwordchange'),

    # path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),

    path('passwordchange/',views.password_change,name='passwordchange'),
    # path('passwordchangedone/',Templateview.as_view('app/passwordchangedone.html'))
    path('passwordchangedone/', views.password_change_done, name='passwordchangedone'),



]