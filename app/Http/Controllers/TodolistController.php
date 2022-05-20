<?php

namespace App\Http\Controllers;

use App\Models\todolist;
use Illuminate\Http\Request;


class TodolistController extends Controller
{
    
    public function index()
    {
        //We are going to query all the data to our view
        
        $todolists= todolist::all()->sortBy('lastname');
        return view('home', compact('todolists'));
    }

    
    
    public function store(Request $request)
    {
        //
        $data = $request->validate([
            'content' =>'required',
            'name'=>'required',
            'lastname'=>'required']);

        todolist::create($data);
        return back();
    }

    
    public function destroy(todolist $todolist)
    {
        //
        $todolist->delete();
        return back();
    }
}
