from django.urls import path
from.import views

urlpatterns=[

    path("",views.home,name="home"),
    
    path("FeedbackView",views.FeedbackView,name="FeedbackView"),
    path("ViewFeedback",views.ViewFeedback,name="ViewFeedback"),
    path("deleteFeedback/<int:id>",views.deleteFeedback,name="deleteFeedback"),
    path("editfeedback/<int:id>",views.editfeedback,name="editfeedback"),
    path("UpdateFeedback/<int:id>",views.UpdateFeedback,name="UpdateFeedback"),
   
    path("about",views.about,name="about"),
    
    path("data",views.data,name="data"),
    path("ViewData",views.ViewData,name="ViewData"),
    path("deletedata/<int:id>",views.deletedata,name="deletedata"),
    path("editdata/<int:id>",views.editdata,name="editdata"),
    path("Updatedata/<int:id>",views.Updatedata,name="Updatedata"),
    
    path("dd",views.dd,name="dd"),
    path("maps",views.maps,name="maps"),
    path("prediction",views.prediction,name="prediction"),
    
     

    ]