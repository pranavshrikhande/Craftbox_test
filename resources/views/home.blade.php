<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE-edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Todo List</title>

        <!--Font Awesome -->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesom/5.15.1/css/all.min.css" rel="stylesheet" />
        <!--MDB-->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.3.0/mdb.min.css" rel="stylesheet" />
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css'>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/mdb-ui-kit/3.3.0/mdb.min.js"></script>
    </head>
    <body class="bg-info">
        <div class="container w-25">

            <div class="">
                <div class="">
                    <h3>Do-it App</h3>
                    
                    <form action="{{ route('store') }}" method="POST" autocomplete="off">
                        @csrf
                        <div class="">
                            <select id="customer" name="content">
                                <option value="Commercial Customer">Commercial Customer</option>
                                <option value="Regular Customer">Regular Customer</option>
                             </select>   




                             
                            <input type = "text" name="name" class="form-control" placeholder="Enter Name"><br/>
                            <input type = "text" name="lastname" class="form-control" placeholder="Enter Last Name"><br/>
                            <button type="submit" class="btn btn-dark"><i class="glyphicon glyphicon-plus-sign" style="font-size:20px"></i></button>
                            
                        </div>

                    
                    </form>

                    {{--if tasks count--}}
                    @if (count($todolists))
                    <ul class="list-group list-group-flush mt-5">
                        @foreach ($todolists as $todolist)
                        
                            <li class="list-group-item border border-dark">

                                <form action = "{{ route('destroy', $todolist->id) }}" method="POST">
                                    
                                    {{ $todolist->content }}
                                    {{ $todolist->name }}
                                    {{ $todolist->lastname }}
                                    @csrf
                                    @method("delete")
                                    <button type="submit" class="btn btn-dark btn-sm float-end"><i class='bi bi-trash'></i></button>

                                </form>
                                
                            </li>
                        
                        @endforeach
                        </ul>
                        @else
                        <p class="text-center mt-3">No list!</p>

                        @endif
                </div>
                @if (count($todolists))
                    <div class="card-footer">
                        You have {{ count($todolists) }} Customers
                    </div>
                @else 

                @endif
            </div>
        </div>
        
    </body>
</html>
