from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'chat/index.html'


class RoomView(TemplateView):
    template_name = 'chat/room.html'

    def get_context_data(self, room_name, **kwargs):
        return {'room_name': room_name}
