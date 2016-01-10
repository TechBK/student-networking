from django.views import generic
from django.http import JsonResponse
from .models import Note, Tag, NoteText
from django.forms import modelform_factory
from .forms import NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin

class NotesView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/login/'
    template_name = 'notes/index.html'

    def get_query(self):
        """
        Cho nay chua toi uu phan truy van notes
        :return:
        """
        notes = Note.objects.filter(user = self.request.user)
        return notes

    def get_context_data(self, **kwargs):
        context = super(NotesView,self).get_context_data(**kwargs)
        context['notes'] = self.get_query()
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            noteform = NoteForm(request.POST)


            if noteform.is_valid():
                note = Note(noteform)
                for tag in noteform['tag']:
                    note.tag_set.add(tag)
