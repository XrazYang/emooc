from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse

from pure_pagination import Paginator, PageNotAnInteger

from apps.organization.models import CourseOrg, City
from apps.organization.forms import AddAskForm

from apps.operation.models import UserFavorite


class OrgDescView(View):
    def get(self, request, org_id, *args, **kwargs):
        current_page = "org_desc"
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()

        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        return render(request, "org-detail-desc.html", {
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav
        })


class OrgCourseView(View):
    def get(self, request, org_id, *args, **kwargs):
        current_page = "org_course"
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()

        all_courses = course_org.course_set.all()

        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        # 对课程机构数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, per_page=1, request=request)
        courses = p.page(page)

        return render(request, "org-detail-course.html", {
            "all_courses": courses,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav
        })


class OrgTeacherView(View):
    def get(self, request, org_id, *args, **kwargs):
        current_page = "org_teacher"
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()

        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_teachers = course_org.teacher_set.all()
        return render(request, "org-detail-teachers.html", {
            "all_teachers": all_teachers,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav
        })


class OrgHomeView(View):
    def get(self, request, org_id, *args, **kwargs):
        current_page = "org_home"
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()

        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True

        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]

        return render(request, "org-detail-homepage.html", {
            "all_courses": all_courses,
            "all_teachers": all_teachers,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav
        })


class AddAskView(View):
    def post(self, request, *args, **kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse({
                "status": "fail",
                "msg": "添加出错"
            })


class OrgView(View):
    def get(self, request, *args, **kwargs):
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()

        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        # 对课程机构进行筛选
        category = request.GET.get("ct", "")
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 通过所在城市对课程机构进行筛选
        city_id = request.GET.get("city", "")
        if city_id:
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))

        # 对机构进行排序
        sort = request.GET.get("sort", "")
        if sort == "students":
            all_orgs = all_orgs.order_by("-students")
        elif sort == "courses":
            all_orgs = all_orgs.order_by("-course_nums")

        org_nums = len(all_orgs)

        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, per_page=1, request=request)
        orgs = p.page(page)

        return render(request, 'org-list.html',
                      {"all_orgs": orgs, 'org_nums': org_nums, 'all_citys': all_citys, "category": category,
                       "city_id": city_id, "sort": sort, "hot_orgs": hot_orgs})

        # 从数据库中获取数据
        # all_orgs = CourseOrg.objects.all()
        # all_citys = City.objects.all()
        # hot_orgs = all_orgs.order_by("-click_nums")[:3]
        #
        # keywords = request.GET.get("keywords", "")
        # s_type = "org"
        # if keywords:
        #     all_orgs = all_orgs.filter(Q(name__icontains=keywords) | Q(desc__icontains=keywords))
        #
        # # 通过机构类别对课程机构进行筛选
        # category = request.GET.get("ct", "")
        # if category:
        #     all_orgs = all_orgs.filter(category=category)
        #
        # # 通过所在城市对课程机构进行筛选
        # city_id = request.GET.get("city", "")
        # if city_id:
        #     if city_id.isdigit():
        #         all_orgs = all_orgs.filter(city_id=int(city_id))
        #
        # # 对机构进行排序
        # sort = request.GET.get("sort", "")
        # if sort == "students":
        #     all_orgs = all_orgs.order_by("-students")
        # elif sort == "courses":
        #     all_orgs = all_orgs.order_by("-course_nums")
        #
        # org_nums = all_orgs.count()
        # # 对课程机构数据进行分页
        # # try:
        # #     page = request.GET.get('page', 1)
        # # except PageNotAnInteger:
        # #     page = 1
        # #
        # # p = Paginator(all_orgs, per_page=1, request=request)
        # # orgs = p.page(page)
        # return render(request, "org-list.html", {
        #     # "all_orgs": orgs,
        #     "org_nums": org_nums,
        #     "all_citys": all_citys,
        #     "category": category,
        #     "city_id": city_id,
        #     "sort": sort,
        #     "hot_orgs": hot_orgs,
        #     "keywords": keywords,
        #     "s_type": s_type
        # })
