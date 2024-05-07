In [3]: models.User.objects.all()
Out[3]: <QuerySet [<User: User object (2)>, <User: User object (1)>]>

In [4]: models.User.objects.order_by('-created_at')[:10]
Out[4]: <QuerySet [<User: User object (2)>, <User: User object (1)>]>

In [5]: models.User.objects.order_by('name')
Out[5]: <QuerySet [<User: User object (1)>, <User: User object (2)>]>

In [6]: models.User.objects.filter(email='pervi@gmail.com')
Out[6]: <QuerySet [<User: User object (1)>]>

In [7]: models.User.objects.filter(created_at__range=['2024-01-01', '2024-12-31'])
/Users/tyu00/PycharmProjects/ProjectDjango/.venv/lib/python3.12/site-packages/django/db/models/fields/__init__.py:1659: RuntimeWarning: DateTimeField User.created_at received a naive datetime (2024-01-01 00:00:00) while time zone support is active.
  warnings.warn(
/Users/tyu00/PycharmProjects/ProjectDjango/.venv/lib/python3.12/site-packages/django/db/models/fields/__init__.py:1659: RuntimeWarning: DateTimeField User.created_at received a naive datetime (2024-12-31 00:00:00) while time zone support is active.
  warnings.warn(
Out[7]: <QuerySet [<User: User object (2)>, <User: User object (1)>]>

In [8]: models.Post.objects.filter(author__name='Первый')
Out[8]: <QuerySet [<Post: Post object (2)>]>

In [9]: models.Tag.objects.filter(posts__isnull=True)
Out[9]: <QuerySet [<Tag: Tag object (4)>]>

In [10]: models.Post.objects.all()
Out[10]: <QuerySet [<Post: Post object (2)>, <Post: Post object (1)>]>

In [11]: models.User.objects.filter(created_at__year=2024)
Out[11]: <QuerySet [<User: User object (2)>, <User: User object (1)>]>

In [12]: models.Post.objects.filter(image__isnull=True)
Out[12]: <QuerySet []>

In [13]: models.Tag.objects.filter(posts__author__name='Первый').distinct()
Out[13]: <QuerySet [<Tag: Tag object (1)>]>

In [14]: models.Post.objects.get(id=1).tags.all()
Out[14]: <QuerySet [<Tag: Tag object (3)>]>

In [15]: models.User.objects.filter(posts__tags__name='новости').distinct()
Out[15]: <QuerySet []>

In [16]: models.Tag.objects.filter(name__istartswith='н')
Out[16]: <QuerySet [<Tag: Tag object (4)>]>

In [17]: models.User.objects.filter(bio__isnull=True)
Out[17]: <QuerySet []>

In [18]: models.Tag.objects.order_by('created_at')
Out[18]: <QuerySet [<Tag: Tag object (1)>, <Tag: Tag object (3)>, <Tag: Tag object (4)>]>

In [19]: models.User.objects.filter(email__icontains='@gmail.com')
Out[19]: <QuerySet [<User: User object (1)>]>

In [20]: models.Post.objects.order_by('-title')
Out[20]: <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>

In [21]: models.User.objects.filter(name__icontains='Пер')
Out[21]: <QuerySet [<User: User object (1)>]>

In [22]: models.User.objects.filter(created_at__gt='2024-01-01')
/Users/tyu00/PycharmProjects/ProjectDjango/.venv/lib/python3.12/site-packages/django/db/models/fields/__init__.py:1659: RuntimeWarning: DateTimeField User.created_at received a naive datetime (2024-01-01 00:00:00) while time zone support is active.
  warnings.warn(
Out[22]: <QuerySet [<User: User object (2)>, <User: User object (1)>]>

In [23]: models.Tag.objects.filter(name__regex=r'^\d+$')
Out[23]: <QuerySet []>

In [24]: models.Post.objects.filter(content__icontains='helldivers 2')
Out[24]: <QuerySet [<Post: Post object (2)>]>

In [25]: models.User.objects.filter(phone__isnull=True)
Out[25]: <QuerySet [<User: User object (2)>]>

