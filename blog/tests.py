from django.test import TestCase
from django.urls import resolve
from blog.views import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException


# Before running Tests, remove the @login_required in views.py, which is used for autherisation purpose.
class FunctionalTests(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'/Users/fahadhabibalwaheedi/Desktop/University/SecondYear/BridgeCourseWork/brdgassign/myvenv/bin/geckodriver')

    def test_cvpage_url(self):
        self.browser.get('http://localhost:8000/cv')
        self.assertIn('Fahad Habib Al Waheedi',self.browser.page_source)

    def test_mainpage_button_redirect(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_xpath("/html/body/center/div[2]/button[2]/a").click()
        self.assertIn('http://localhost:8000/cv',self.browser.current_url)

    def test_wrkexp_url(self):
        self.browser.get('http://localhost:8000/cv/work_experience/')
        self.assertIn('Work Experience',self.browser.page_source)

    def test_wrkexp_redirect(self):
        self.browser.get('http://localhost:8000/cv')
        self.browser.find_element_by_id("wrkexpbutton").click()
        self.assertIn('http://localhost:8000/cv/work_experience',self.browser.current_url)

    def test_education_url(self):
        self.browser.get('http://localhost:8000/cv/education/')
        self.assertIn('Education',self.browser.page_source)

    def test_edu_redirect(self):
        self.browser.get('http://localhost:8000/cv')
        self.browser.find_element_by_id("edu").click()
        self.assertIn('http://localhost:8000/cv/education',self.browser.current_url)

    def test_project_url(self):
        self.browser.get('http://localhost:8000/cv/project/')
        self.assertIn('Projects',self.browser.page_source)

    def test_prj_redirect(self):
        self.browser.get('http://localhost:8000/cv')
        self.browser.find_element_by_id("prj").click()
        self.assertIn('http://localhost:8000/cv/project',self.browser.current_url)

    def test_formpage_url(self):
        self.browser.get('http://localhost:8000/cv/new/')
        self.assertIn('Add/Edit CV Element',self.browser.page_source)

    def test_formpage_redirect(self):
        self.browser.get('http://localhost:8000/cv')
        self.browser.find_element_by_id("secretbutton").click()
        self.assertIn('http://localhost:8000/cv/new/',self.browser.current_url)

    def test_formpage_addwrkexp(self):
        self.browser.get('http://localhost:8000/cv/new')
        typeSelect = Select(self.browser.find_element_by_name('type'))
        typeSelect.select_by_visible_text('Work Experience')
        name = self.browser.find_element_by_name("name")
        name.send_keys("Test Added Successfully Work Experience")
        employer = self.browser.find_element_by_name("emplyInti")
        employer.send_keys("Test Employer")
        fromDate = self.browser.find_element_by_name("fromDate")
        fromDate.send_keys("2020-06-10")
        toDate = self.browser.find_element_by_name("toDate")
        toDate.send_keys("Present")
        description = self.browser.find_element_by_name("description")
        description.send_keys("This is a test description")
        self.browser.find_element_by_id("formsubmit").click()
        self.assertIn('Test Added Successfully Work Experience',self.browser.page_source)

    def test_formpage_addedu(self):
        self.browser.get('http://localhost:8000/cv/new')
        typeSelect = Select(self.browser.find_element_by_name('type'))
        typeSelect.select_by_visible_text('Education')
        name = self.browser.find_element_by_name("name")
        name.send_keys("Test Added Successfully Education")
        school = self.browser.find_element_by_name("emplyInti")
        school.send_keys("Test Education")
        description = self.browser.find_element_by_name("description")
        description.send_keys("This is a test description")
        self.browser.find_element_by_id("formsubmit").click()
        self.assertIn('Test Added Successfully Education',self.browser.page_source)

    def test_formpage_addprj(self):
        self.browser.get('http://localhost:8000/cv/new')
        typeSelect = Select(self.browser.find_element_by_name('type'))
        typeSelect.select_by_visible_text('Projects')
        name = self.browser.find_element_by_name("name")
        name.send_keys("Test Added Successfully Project")
        description = self.browser.find_element_by_name("description")
        description.send_keys("This is a test description")
        self.browser.find_element_by_id("formsubmit").click()
        self.assertIn('Test Added Successfully Project',self.browser.page_source)

    def test_wrkexp_formedit(self):
        self.browser.get('http://localhost:8000/cv/work_experience')
        self.browser.find_element_by_id("wrkexpedit").click()
        name = self.browser.find_element_by_name("name")
        name.clear()
        name.send_keys("Work Experience edited successfully")
        employer = self.browser.find_element_by_name("emplyInti")
        employer.clear()
        employer.send_keys("Employer Successfully edited")
        description = self.browser.find_element_by_name("description")
        description.send_keys("Edited test description")
        self.browser.find_element_by_id("formsubmit").click()
        self.assertIn('Work Experience edited successfully',self.browser.page_source)

    def test_edu_formedit(self):
        self.browser.get('http://localhost:8000/cv/education')
        self.browser.find_element_by_id("eduedit").click()
        name = self.browser.find_element_by_name("name")
        name.clear()
        name.send_keys("Education edited successfully")
        institute = self.browser.find_element_by_name("emplyInti")
        institute.clear()
        institute.send_keys("Institute Successfully edited")
        description = self.browser.find_element_by_name("description")
        description.send_keys("Edited test description")
        self.browser.find_element_by_id("formsubmit").click()
        self.assertIn('Education edited successfully',self.browser.page_source)


    def test_prj_formedit(self):
        self.browser.get('http://localhost:8000/cv/project')
        self.browser.find_element_by_id("prjedit").click()
        name = self.browser.find_element_by_name("name")
        name.clear()
        name.send_keys("Project edited successfully")
        self.browser.find_element_by_id("formsubmit").click()
        self.assertIn('Project edited successfully',self.browser.page_source)

    def test_wrkexp_delete(self):
        self.browser.get('http://localhost:8000/cv/work_experience')
        self.browser.find_element_by_id("wrkdelete").click()
        try:
            self.browser.find_element_by_xpath("//*[contains(text(), 'Work Experience edited successfully')]")
            return False
        except NoSuchElementException:
            return True

    def test_edu_delete(self):
        self.browser.get('http://localhost:8000/cv/education')
        self.browser.find_element_by_id("edudelete").click()
        try:
            self.browser.find_element_by_xpath("//*[contains(text(), 'Education edited successfully')]")
            return False
        except NoSuchElementException:
            return True

    def test_prj_delete(self):
        self.browser.get('http://localhost:8000/cv/project')
        self.browser.find_element_by_id("prjdelete").click()
        try:
            self.browser.find_element_by_xpath("//*[contains(text(), 'Project edited successfully')]")
            return False
        except NoSuchElementException:
            return True

    def tearDown(self):
        self.browser.quit()

# Before running Tests, remove the @login_required in views.py, which is used for autherisation purpose.
class UnitTests(TestCase):

    def test_cvpage_url_resolve_func(self):
        find = resolve('/cv/')
        self.assertEqual(find.func, cvmenu )

    def test_cvpage_template(self):
        result = self.client.get('/cv/')
        self.assertTemplateUsed(result, 'blog/cvpage.html')

    def test_wrkexp_url_resolve_func(self):
        find = resolve('/cv/work_experience/')
        self.assertEqual(find.func, cvwork )

    def test_wrkexp_template(self):
        result = self.client.get('/cv/work_experience/')
        self.assertTemplateUsed(result, 'blog/cvwork.html')

    def test_education_url_resolve_func(self):
        find = resolve('/cv/education/')
        self.assertEqual(find.func, cvedu)

    def test_education_template(self):
        result = self.client.get('/cv/education/')
        self.assertTemplateUsed(result, 'blog/cvedu.html')

    def test_prj_url_resolve_func(self):
        find = resolve('/cv/project/')
        self.assertEqual(find.func, cvproj)

    def test_prj_template(self):
        result = self.client.get('/cv/project/')
        self.assertTemplateUsed(result, 'blog/cvproj.html')

    def test_formpage_add_url_resolve_func(self):
        find = resolve('/cv/new/')
        self.assertEqual(find.func, addnew)

    def test_formpage_add_template(self):
        result = self.client.get('/cv/new/')
        self.assertTemplateUsed(result, 'blog/addcvelem.html')

    def test_formpage_edit_url_resolve_func(self):
        elem = CVElem.objects.create()
        find = resolve('/post/edit/%d/' % (elem.id,))
        self.assertEqual(find.func, editcvelem)

    def test_formpage_edit_template(self):
        elem = CVElem.objects.create()
        result = self.client.get('/post/edit/%d/' % (elem.id,))
        self.assertTemplateUsed(result, 'blog/addcvelem.html')
