from django.shortcuts import render, redirect

contact_list = []


def contacts(request):

    return render(request, 'contacts.html', {'name': 'Leonardo', 'contacts': contact_list})


def add_contact(request):
    if request.method == 'POST':
        contact_list.append(request.POST['contact'])
        return redirect('/contacts/')

    return render(request, 'add_contact.html')
