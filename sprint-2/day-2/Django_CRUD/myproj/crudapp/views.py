from django.shortcuts import render, redirect

# Create your views here.
data = [
    {"name":"Arun",'age':20,'city':'bangalore'},
    {"name":"Amal",'age':20,'city':'bangalore'}
]
def create_view(request):
    if request.method == "POST":
        name = request.POST['name']
        age = int(request.POST['age'])
        city  = request.POST['city']

        new_entry = {
            'name': name,
            'age': age,
            'city': city
        }
        data.append(new_entry)

    return render(request, 'crud/create.html')

def read_view(request):
    return render(request, 'crud/read.html', {'data': data})
 
def update_view(request, name):
    entry = None
    for item in data:
        if item['name'] == name:
            entry = item
            break
    if request.method == 'POST':
        new_age = int(request.POST['new_age'])
        new_city = request.POST['new_city']
        entry['age'] = new_age
        entry['city'] = new_city

    return render(request, 'crud/update.html', {'entry': entry})

def delete_view(request, name):
    global data
    data = [entry for entry in data if entry['name'] != name]
    return redirect('read_view')