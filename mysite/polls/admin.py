from .models import *
from django.contrib import admin
# Register your models here.
from .models import Question, Choice, Survey
from .forms import SurveyForm

from django.utils.safestring import mark_safe
from django.urls import reverse

import nested_admin


class TocArticleInline(nested_admin.NestedStackedInline):
    model = Choice
    #sortable_field_name = "position"


class TocSectionInline(nested_admin.NestedStackedInline):
    model = Question
    #sortable_field_name = "position"
    inlines = [TocArticleInline]


class SurveyAdmin(nested_admin.NestedModelAdmin):
    inlines = [TocSectionInline]


admin.site.register(Survey, SurveyAdmin)

#from django.core.urlresolvers import reverse
#from django.utils.translation import ugettext_lazy as _
#from django.utils.text import force_text

'''
def get_picture_preview(obj):
    if obj.pk:  # if object has already been saved and has a primary key, show picture preview
        return """<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
            src=obj.picture.url,
            title=obj.title,
        )
    return _("(choose a picture and save and continue editing to see the preview)")
get_picture_preview.allow_tags = True
get_picture_preview.short_description = _("Picture Preview")



class PictureInline(admin.StackedInline):
    model = Survey
    extra = 0
    #fields = ["get_edit_link", "title", "picture", get_picture_preview]
    #readonly_fields = ["get_edit_link", get_picture_preview]
    readonly_fields = ["get_edit_link"]

    def get_edit_link(self, obj=None):
        if obj.pk:  # if object has already been saved and has a primary key, show link to it
            url = reverse(
                'admin:%s_%s_change' % (
                    obj._meta.app_label, obj._meta.model_name),
                args=[force_text(obj.pk)]
            )
            return mark_safe("""<a href="{url}">{text}</a>""".format(
                url=url,
                text=_("Edit this %s separately") % obj._meta.verbose_name,
            ))
        return _("(save and continue editing to create a link)")
    #get_edit_link.short_description = _("Edit link")


# @admin.register(Painter)
class PainterAdmin(admin.ModelAdmin):
    save_on_top = True
    #fields = ["name"]
    inlines = [PictureInline]


class ReviewInline(admin.StackedInline):
    model = Choice
    extra = 0
    #fields = ["reviewer", "comment"]


# @admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    save_on_top = True
    #fields = ["painter", "title", "picture", get_picture_preview]
    #readonly_fields = [get_picture_preview]
    inlines = [ReviewInline]


admin.site.register(Survey, PictureAdmin)
admin.site.register(Question)
admin.site.register(Choice)
'''
'''
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class EditLinkToInlineObject(object):
    def edit_link(self, instance):
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk])
        if instance.pk:
            return mark_safe(u'<a href="{u}">edit</a>'.format(u=url))
        else:
            return ''


class MyModelInline(EditLinkToInlineObject, admin.TabularInline):
    model = Question
    inlines = [ChoiceInLine]
    readonly_fields = ('edit_link', )


class MySecondModelAdmin(admin.ModelAdmin):
    inlines = (MyModelInline, )


admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Survey, MySecondModelAdmin)
'''

'''
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionInLine(admin.TabularInline):
    model = Question
    inlines = [ChoiceInLine]

    ''''''
    fieldsets = [
        (None, {'fields': ['question_text']}),
    ]
    



    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']  # side bar box
    search_fields = ['question_text']   # search form box
''''''


class SurveyAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['survey_title']}),
        (None, {'fields': ['survey_description']}),
    ]

    inlines = [QuestionInLine]
    list_display = ('survey_title', 'survey_description')


admin.site.register(Survey, SurveyAdmin)

admin.site.register(Question)
admin.site.register(Choice)


''''''
# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        #('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'was_published_recently')
    list_filter = ['pub_date']  # side bar box
    search_fields = ['question_text']   # search form box


admin.site.register(Question, QuestionAdmin)
''''''

'''
