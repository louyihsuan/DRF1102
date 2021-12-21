# DRF1102 - Django rest framework

This is a demo of DRF

The scenario is about design the vidoes platform like Youtube, Netflix.


 
> Drf
> 
> PostgreSQL
> 
> Redis
> 
> Celery
> 
> apschedule


{

    "users": "http://127.0.0.1:8000/api/users/",
    
    "videos": "http://127.0.0.1:8000/api/videos/",
    
    "comments": "http://127.0.0.1:8000/api/comments/",
    
    "vcs": "http://127.0.0.1:8000/api/vcs/"
    
}


/api/videos/pk/vdetail/

/api/videos/vrank/

/api/videos/vtopsendmail/ - sendmail with celery in unsync ways


/api/vcs/pk/vcdetail/  - rawsql query in id

/api/vcs/vcall/ - rawsql query all
