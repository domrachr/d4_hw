from p_library.models import Author, Book
all_books = Book.objects.all()
max_price = 0.0
for book in all_books:
    if book.price > max_price

all_books_price = 0
for book in Book.objects.filter(copy_count__gt=1):
    all_books_price += book.price * book.copy_count

Book.objects.annotate(num_authors=Count('author')).filter(num_authors__gt=1)

from django.db.models import Avg, Count, Min, Sum, FloatField, F
authors_= Author.objects.annotate(num_books=Count('book', distinct=True)).filter(num_books__gt=1)
sum_all = 0.0
for author in authors_:
    sum_all += Book.objects.filter(author=author).aggregate(price_all=Sum(F('price') * F('copy_count'), output_field=FloatField()))['price_all']
print(sum_all)


from django.db.models import Avg, Count, Min, Sum, FloatField, F
authors_= Author.objects.exclude(country__icontains='ru')
sum_all = 0.0
for author in authors_:
    sum_all += Book.objects.filter(author=author).aggregate(price_all=Sum(F('price') * F('copy_count'), output_field=FloatField()))['price_all']

print(sum_all)


from django.db.models import Avg, Count, Min, Sum, FloatField, F
pushkin = Author.objects.get(full_name="Пушкин Александр Сергеевич")
Book.objects.filter(author=pushkin).aggregate(price_all=Sum(F('price') * F('copy_count'), output_field=FloatField()))['price_all']

print(sum_all)


from django.db.models import Avg, Count, Min, Sum, FloatField, F
douglas = Author.objects.get(full_name="Douglas Adams")
Book.objects.filter(author=douglas).aggregate(price_all=Sum(F('price'), output_field=FloatField()))['price_all']

print(sum_all)