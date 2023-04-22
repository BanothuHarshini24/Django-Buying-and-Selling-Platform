from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,signed,post,wishlist,cart,verify_post,myorders,week_bid,reports,not_verify
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from datetime import datetime,timedelta
from django.utils import timezone
import uuid
from django.contrib.auth.hashers import make_password,check_password
# import pyotp

# Create your views here.
today = timezone.now().strftime('%A')

def verify(request):
    posts=verify_post.objects.all()
    return render(request,'verify.html',{'posts':posts})

def approve(request):
     post_id=request.GET.get('post_id')
     Post=verify_post.objects.get(id_post=post_id)
     new_post=post.objects.create(user=Post.user,title=Post.title,category=Post.category,location=Post.location,description=Post.description,price=Post.price,image1=Post.image1,image2=Post.image2,image3=Post.image3,image4=Post.image4,image5=Post.image5,id_post=Post.id_post,bid_price=Post.bid_price)
     new_post.save()
     Post.delete()
     return redirect('verify')

def notapprove(request):
    post_id=request.GET.get('post_id')
    Post=verify_post.objects.get(id_post=post_id)
    Post.verification=False
    new_post=not_verify.objects.create(user=Post.user,title=Post.title,category=Post.category,location=Post.location,description=Post.description,price=Post.price,image1=Post.image1,image2=Post.image2,image3=Post.image3,image4=Post.image4,image5=Post.image5,id_post=Post.id_post,bid_price=Post.bid_price)
    new_post.verification=False
    Post.delete()
    return redirect('verify')

def index(request):
    feed=post.objects.all()
    return render(request,'index.html',{'feed':feed})

def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        x=email.split('@')
        y="iiti.ac.in"
        if y in x:
            full_name=request.POST['full_name']
            username=request.POST['username']
            password=request.POST['password']
            password2=request.POST['password2']
            phone_number=request.POST['phone_number']
            if password== password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'email already exists')
                    return redirect('signup')
                elif User.objects.filter(username=username).exists():
                    messages.info(request,'username already exists')
                    return redirect('signup')
                elif len(phone_number)!=10:
                    messages.info(request,'invalid phonenumber')
                    return redirect('signup')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    signed_user=signed.objects.create(full_name=full_name,username=username,email=email,password=password,phone_number=phone_number)
                    signed_user.save()
                    user_login=auth.authenticate(username=username,password=password)
                    auth.login(request,user_login)
                    user_model=User.objects.get(username=username)
                    new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                    new_profile.save()
                    #recipient = request.POST.get('recipient')
                    subject = "CONFIRMATION EMAIL"
                    message = "YOU HAVE SUCCESSFULLY LOGGED IN"
                    send_mail(
                    subject,
                    message,
                    'nimmanagotiroopasri@gmail.com',
                    [email],
                    fail_silently=False,
                    )
                    return redirect('/')
            else:
                messages.info(request,'password is not matching')
                return redirect('signup')
        else:
            messages.info(request,"invalid email_id")
            return redirect('signup')   
        
    else:
        return render (request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Please enter a valid email/password')
            return redirect('login')
    else:
        return render(request,'login.html')

@login_required(login_url='login')
def listing(request):
    if request.method=='POST':
        title=request.POST['title']
        category=request.POST['category']
        location=request.POST['location']
        description=request.POST['description']
        price=request.POST['price']
        img1=request.FILES.get('img1')
        img2=request.FILES.get('img2')
        img3=request.FILES.get('img3')
        img4=request.FILES.get('img4')
        img5=request.FILES.get('img5')
        bidprice = request.POST['bidprice']
        new_verify_post=verify_post.objects.create(title=title,user=request.user.username,category=category,location=location,description=description,price=price,image1=img1,image2=img2,image3=img3,image4=img4,image5=img5,bid_price=bidprice)
        new_verify_post.save()
        messages.info(request,"Kindly wait until admin approve your post...")
        return redirect('listing')
    else:
        return render(request,'listing.html')

@login_required(login_url='login')
def display(request):
    post_id=request.GET.get('post_id')
    display_post=post.objects.get(id_post=post_id)
    signed_user=signed.objects.get(username=display_post.user)
    contact_no=signed_user.phone_number
    return render(request,'display.html',{'display_post':display_post,'contact_no':contact_no})

@login_required(login_url='login')
def like(request):
    username=request.user.username
    post_id=request.GET.get('post_id')
    like_filter=wishlist.objects.filter(username=username,post_id=post_id).first()
    if like_filter==None:
        new_liked_post=wishlist.objects.create(username=username,post_id=post_id)
        new_liked_post.save()
        liked_post=post.objects.get(id_post=post_id)
        liked_post.likes=liked_post.likes+1
        liked_post.save()
        return render(request,'display.html',{'display_post':liked_post})
    else:
        like_filter.delete()
        liked_post=post.objects.get(id_post=post_id)
        liked_post.likes=liked_post.likes-1
        liked_post.save()
        return render(request,'display.html',{'display_post':liked_post})

@login_required(login_url='login')
def like1(request):
    username=request.user.username
    post_id=request.GET.get('post_id')
    like_filter=wishlist.objects.filter(username=username,post_id=post_id).first()
    if like_filter==None:
        new_liked_post=wishlist.objects.create(username=username,post_id=post_id)
        new_liked_post.save()
        liked_post=post.objects.get(id_post=post_id)
        liked_post.likes=liked_post.likes+1
        liked_post.save()
        return redirect('/')
    else:
        like_filter.delete()
        liked_post=post.objects.get(id_post=post_id)
        liked_post.likes=liked_post.likes-1
        liked_post.save()
        return render(request,'wishlist.html')

@login_required(login_url='login')
def wish(request):
    username=request.user.username
    user_list=wishlist.objects.filter(username=username)
    wish_list=[]
    if user_list==None:
        return render(request,'wishlist.html',{'wish_list':wish_list})
    for l in user_list:
        Post=post.objects.get(id_post=l.post_id)
        wish_list.append(Post)
    return render(request,'wishlist.html',{'wish_list':wish_list})

@login_required(login_url='login')
def carts(request):
    username=request.user.username
    post_id=request.GET.get('post_id')
    cart_object=cart.objects.filter(username=username,post_id=post_id).first()
    Post=post.objects.get(id_post=post_id)
    if cart_object==None:
        new_cart=cart.objects.create(username=username,post_id=post_id)
        new_cart.save()
        Post.cart=Post.cart+1
        Post.save()
        return render(request,'display.html',{'display_post':Post})
    else:
        return render(request,'display.html',{'display_post':Post})

@login_required(login_url='login')
def carts1(request):
    username=request.user.username
    post_id=request.GET.get('post_id')
    cart_object=cart.objects.filter(username=username,post_id=post_id).first()
    Post=post.objects.get(id_post=post_id)
    if cart_object==None:
        new_cart=cart.objects.create(username=username,post_id=post_id)
        new_cart.save()
        Post.cart=Post.cart+1
        Post.save()
        return redirect('/')
    else:
        return redirect('/')
    

@login_required(login_url='login')
def mycart(request):
    username=request.user.username
    add_to_cart=[]
    price=0
    cart_list=cart.objects.filter(username=username)
    for c in cart_list:
        Post=post.objects.get(id_post=c.post_id)
        price=price+Post.price
        add_to_cart.append(Post)
    
    return render(request,'mycart.html',{'add_to_cart':add_to_cart,'price':price})

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='login')
def mysales(request):
     Post=post.objects.filter(user=request.user.username)
     return render(request,'mysales.html',{'Post':Post})

@login_required(login_url='login')
def remove_cart(request):
    post_id=request.GET.get('post_id')
    Post=cart.objects.filter(post_id=post_id)
    Post.delete()
    return redirect('mycart')

def search(request):
    keywords=request.GET['keywords']
    allPosts= post.objects.filter(title__icontains=keywords)
    if allPosts:
         text=''
    else:
         text='not found'
         print(text)
    return render(request,'search.html',{'allposts':allPosts,'text':text, 'keywords':keywords})

def forgot_pwd(request):
    return render(request,'forgot_pwd.html')


# def send_otp(request):
#     secret_key = pyotp.random_base32()
#     ver_mail=request.POST['email']
#     user=User.objects.get(email=ver_mail)
#     if user is not None:
#         profile=Profile.objects.get(user=user)
#         profile.secret_key=secret_key
#         profile.save()
#         otp = generate_totp(secret_key)
#         subject = "OTP"
#         message = otp
#         send_mail(
#             subject,
#             message,
#             'nimmanagotiroopasri@gmail.com',
#             [ver_mail],
#             fail_silently=False,
  
#         return render(request,'enter_otp.html')
#     else:
#         return redirect('signup')

# def verify_otp(request):
#     ver_mail = request.session.get('ver_mail')
#     user=User.objects.get(email=ver_mail)
#     profile=Profile.objects.get(user=user)
#     entered_otp=request.POST['otp']
#     s_key=profile.secret_key
#     otp1=generate_totp(s_key)
#     if otp1==entered_otp:
#         return render(request,'new_pwd.html')
#     else:
#         messages.info(request,"otp is not matched")
#         return redirect('forgot_pwd')

# def send_otp(request):
#     # Generate secret key and OTP
#     secret_key = pyotp.random_base32()
#     otp = generate_totp(secret_key)

    # Store secret key and OTP in user's profile
    # ver_mail = request.POST['email']
    # user = User.objects.get(email=ver_mail)
    # profile = Profile.objects.get(user=user)
    # profile.secret_key = secret_key 
    # print(secret_key)
    # print(otp)
    # profile.save()

    # # Send OTP to user's email address
    # subject = "OTP"
#     message = otp
#     send_mail(subject, message, 'nimmanagotiroopasri@gmail.com', [ver_mail], fail_silently=False)

#     # Store email address in session for verification
#     request.session['ver_mail'] = ver_mail

#     # Render enter_otp.html template
#     return render(request, 'enter_otp.html')

# def verify_otp(request):
#     # Retrieve email address from session
#     ver_mail = request.session.get('ver_mail')

#     # Retrieve user and profile from database
#     user = User.objects.get(email=ver_mail)
#     profile = Profile.objects.get(user=user)
    
    # # Retrieve OTP entered by user
    # entered_otp = request.POST['otp']
    # print(entered_otp)
    # # Generate TOTP using secret key
    # s_key = profile.secret_key
    # otp1 = generate_totp(s_key)
    # print(s_key)
    # print(otp1)

    # # Compare OTPs and proceed accordingly
    # if otp1==entered_otp:
    #     # Clear email address from session
    #     # del request.session['ver_mail']

    #     # Render new_pwd.html template
    #     return render(request, 'new_pwd.html')
    # else:
    #     # Render forgot_pwd.html template with error message
    #     return redirect('forgot_pwd')


def new_pwd(request):
  if request.method=='POST':
    password=request.POST['password']
    ver_mail = request.session.get('ver_mail')
    user=User.objects.get(email=ver_mail)
    user.password=password
    user.save()
    signed_user=signed.objects.get(email=ver_mail)
    signed_user.password=password
    signed_user.save()
    del request.session['ver_mail']
    return render(request,'login.html')
  else:
    return render(request,'new_pwd.html')

def remove_post(request):
    post_id=request.GET.get('post_id')
    Post=post.objects.get(id_post=post_id)
    Post.delete()
    w=wishlist.objects.all()
    for w in w:
        if w.post_id==post_id:
           w.delete()
    c=cart.objects.all()
    for d in c:
        if d.post_id==post_id:
           d.delete()
    b=week_bid.objects.all()
    for b in b:
        if b.post_id==post_id:
            b.delete()
    r=reports.objects.all()
    for r in r:
        if r.post_id==post_id:
           r.delete()
    return redirect('mysales')

def purchase(request):
    post_id=request.GET.get('post_id')
    Post=post.objects.get(id_post=post_id)
    #delete post
    return render(request,'purchase.html',{'Post':Post})

def cart_purchase(request):
     cart_list=cart.objects.filter(username=request.user.username)
     Post=[]
     price=0
     ver_mail=request.user.email
     for d in cart_list:
       p=post.objects.get(id_post=d.post_id)
       Post.append(p)
       price=price+p.price
       price1=str(price)
       subject = "INVOICE"
       message = "today you have purchased "+ price1
     send_mail(subject, message, 'nimmanagotiroopasri@gmail.com', [ver_mail], fail_silently=False)

     return render(request,'cart_purchase.html',{'post':Post,'price':price})

# def filter(request,pk):
#     allPosts= post.objects.filter(title__icontains=pk)
#     price=request.GET.get('price')
#     latest=request.GET.get('latest')
#     if price:
#        allPosts= post.objects.filter(title__icontains=pk)
#        sorted_array=allPosts.objects.all().order_by('price')
#     return render(request,'filter.html',{'sorted_array':sorted_array})

def filter(request,pk):
    return redirect('/')

def orders(request):
    username=request.user.username
    post_id=request.GET.get('post_id')
    new_order=myorders.objects.create(username=username,post_id=post_id)
    new_order.save()
    Post=post.objects.get(id_post=post_id)
    return render(request,'purchase.html',{'post':Post})

def my_orders(request):
    orders=myorders.objects.filter(username=request.user.username)
    order=[]
    for o in orders:
        Post=post.objects.get(id_post=o.post_id)
        order.append(Post)
    return render(request,'myorders.html',{'order':order})


def loginpage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        name="admin"
        pwd="adminpassword"
        if username==name and password==pwd:              
          posts=verify_post.objects.all()
          return render(request,'verify.html',{'posts':posts})
        else:
         messages.info(request,"INVALID CREDENTIALS")
         return redirect('loginpage')
    else:
      return render(request,'loginpage.html')

def bidding(request):
    bid=[]
    bid_price=[]
    if today=="Friday":
        Post=post.objects.all()
        minimum_duration=timedelta(seconds=3600)
        for p in Post:
            if p.duration>minimum_duration:
                bid.append(p)
        return render(request,'bidding.html',{'bid':bid})
    else:
        messages.info(request,'No bidding come on tuesday for bidding')
        return render(request,'bidding.html',{'bid':bid})

@login_required(login_url='login')
def do_bidding(request,pk):
    Post=post.objects.get(id_post=pk)
    bidding_price=request.POST['bidding_price']
    if int(bidding_price)>Post.bid_price:
        Post.bid_price=int(bidding_price)
        Post.save()
        if week_bid.objects.filter(post_id=pk).exists():
           bid_post=week_bid.objects.get(post_id=pk)
           bid_post.username=request.user.username
           bid_post.save()
        else:
            new_bid_post=week_bid.objects.create(post_id=pk,username=request.user.username)
            new_bid_post.save()
    return redirect('bidding')

@login_required(login_url='login')
def notifications(request):
    bid_post=[]
    if today!="Saturday":
        bid_post=week_bid.objects.filter(username=request.user.username)
    return render(request,'notifications.html',{'bid_post':bid_post})

def feed_sorted_by_latest(request):
    latest = post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'latest': latest})

def feed_sorted_by_price(request):
    items = post.objects.all().order_by('-price')
    return render(request, 'index.html', {'items': items})

@login_required(login_url='login')
def bidding_info(request):
    bid_post=[]
    win_bid=[]
    not_verified=[]
    not_verified=not_verify.objects.filter(user=request.user.username)
    if today!="Friday":
        bid_post=week_bid.objects.filter(username=request.user.username)
        if len(bid_post)>0:
         for b in bid_post:
            Post=post.objects.get(id_post=b.post_id)
            win_bid.append(Post)
    return render(request,'notifications.html',{'bid_post':win_bid,'not_verified':not_verified})

@login_required(login_url='login')
def report(request):
    post_id=request.GET.get('post_id')
    Post=post.objects.get(id_post=post_id)
    if reports.objects.filter(username=request.user.username,post_id=post_id,seller=Post.user).exists():
        messages.info(request,"You have already reported it we will take actions regarding it")
        return render(request,'display.html',{'display_post':Post})
    else:
        new_report=reports.objects.create(username=request.user.username,post_id=post_id,seller=Post.user)
        new_report.save()
        messages.info(request,"Reported Successfully")   
        return render(request,'display.html',{'display_post':Post})

@login_required(login_url='login')
def report_info(request):
    report=reports.objects.filter(seller=request.user.username)
    reported_posts=[]
    if len(report)>0:
     for re in report:
        Post=post.objects.get(id_post=re.post_id)
        reported_posts.append(Post)
    return render(request,'report_info.html',{'reported_posts':reported_posts})

def display1(request):
    post_id=request.GET.get('post_id')
    display_post=post.objects.get(id_post=post_id)
    return render(request,'display1.html',{'display_post':display_post})

def bid_purchase(request):
    post_id=request.GET.get('post_id')
    Post=post.objects.get(id_post=post_id)
    Post.delete()
    w=wishlist.objects.all()
    for w in w:
        if w.post_id==post_id:
           w.delete()
    c=cart.objects.all()
    for d in c:
        if d.post_id==post_id:
           d.delete()
    b=week_bid.objects.all()
    for b in b:
        if b.post_id==post_id:
            b.delete()
    r=reports.objects.all()
    for r in r:
        if r.post_id==post_id:
           r.delete()
    return render(request,'bid_purchase.html',{'Post':Post})


