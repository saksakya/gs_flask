from flask import Blueprint, redirect, render_template, g, url_for, flash, request
from flask_login import login_required
from apps.student.form import AllUpdateForm, RegistForm, UpdateForm

from apps.student.models import Student
from apps.app import db

student = Blueprint("student", __name__, template_folder="templates", static_folder="static")

@student.route('/top')
@login_required
def top():
    student_list = db.session.query(Student).all()
    return render_template('student/top.html',student_list=student_list)

@student.route('/regist',methods=['GET','POST'])
@login_required
def regist():
    form = RegistForm()
        
    if form.validate_on_submit():
        print(form.data)
        # 画面からの登録情報の取得
        student = Student(
            number=form.number.data,
            nickname=form.nickname.data,
        )
        
        if student.is_duplicate_number():
            flash('指定の生徒番号は登録済みです。')
            return redirect(url_for('student.regist'))
        
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('student.top'))

    return render_template('student/regist.html', form=form)

@student.route('/editall',methods=['GET','POST'])
@login_required
def edit_all():
    form = AllUpdateForm()
    student_list = db.session.query(Student).all()
    
    if form.all[0].validate_on_submit():
        print(form.all.data)
        # 画面からの登録情報の取得
        # student = Student(
        # number=form.number.data,
        # nickname=form.nickname.data,
        # )
        
        # if student.is_duplicate_number():
        #     flash('指定の生徒番号は登録済みです。')
        #     return redirect(url_for('student.regist'))
        
        # db.session.add(student)
        # db.session.commit()
        # return redirect(url_for('student.top'))
    #print(form.all.data)
    return render_template('student/editall.html',form=form, student_list=student_list)


@student.route('/<id>/edit',methods=['GET','POST'])
@login_required
def edit(id):
    form = UpdateForm()
    post = db.session.query(Student).filter_by(id=id).first()
        
    if form.validate_on_submit():
        student = Student(
            number=form.number.data,
            nickname=form.nickname.data,
        )
        
        if(student.number != post.number):
            flash('生徒番号は変更できません。')
            return redirect(url_for('student.edit',id=id))
        
        post.nickname=student.nickname
        
        db.session.commit()
        
        return redirect(url_for('student.top'))
    
    return render_template('student/edit.html', form=form, post=post)

@student.route('/<id>/delete',methods=['GET','POST'])
@login_required
def delete(id):
    post = db.session.query(Student).filter_by(id=id).first()
    
    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('student.top'))
    
    return render_template('student/delete.html', post=post)

