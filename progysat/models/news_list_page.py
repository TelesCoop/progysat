from typing import List

from django.http import Http404
from django.utils import translation
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.models import Page

from progysat.models.news import News
from progysat.utils import objects_for_current_language


class NewsListPage(RoutablePageMixin, Page):
    class Meta:
        verbose_name = "Page des actualités"
        verbose_name_plural = "Pages des actualités"

    parent_page_types = ["progysat.HomePage"]
    subpage_types: List[str] = []
    max_count_per_parent = 1

    @route(r"^(.*)/$", name="news")
    def access_news_page(self, request, news_slug):
        try:
            news = objects_for_current_language(News).get(slug=news_slug)
        except (News.DoesNotExist, News.MultipleObjectsReturned):
            raise Http404

        modal_images = []
        for block in news.body:
            if block.block_type == "image":
                modal_images.append(block.value)

        return self.render(
            request,
            context_overrides={
                "news": news,
                # There is only one NewsListPage if there is only one language
                "news_page": NewsListPage.for_current_language(),
                "modal_images": modal_images,
            },
            template="progysat/news_page.html",
        )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        current_language = translation.get_language()
        context["news_list"] = [
            news.to_dict()
            for news in News.objects.filter(locale__language_code=current_language)
        ]

        return context

    @staticmethod
    def for_current_language():
        current_language = translation.get_language()
        return NewsListPage.objects.get(locale__language_code=current_language)
