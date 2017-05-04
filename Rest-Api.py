import requests
import json
from flask import Flask,request,jsonify,make_response,abort
app = Flask(__name__)                       
tasks=[]
arr=[]
f=1
ii=0
jj=0
kk=0
@app.route('/')
def index():
    return "Sentiment:Score-Analyser!"

@app.route('/sentiment/')
def sentiment():
    return "Sentiment:Score-Analyser!"  

@app.route('/sentiment/get/', methods=['HEAD'])
def head_task():
     with open('final.json') as f:
      data=json.load(f)     
      if not data:
        return make_response(jsonify({'no-content': 'false'}), 204)
     return jsonify({'Score-card':data})
     
@app.route('/sentiment/get/<string:task_tag>/',methods=['HEAD'])
def head_tas(task_tag):
    with open('final.json') as f:
     data=json.load(f)
    with open('type.json') as f1:
     types=json.load(f1) 
    for i in xrange(len(types)):    
     if types[i]==task_tag:
        return jsonify({'Score-card':data[task_tag]})    
    return make_response(jsonify({'no-content': 'false'}), 204)

@app.route('/sentiment/get/<string:task_tag>/<string:task_tag1>/', methods=['HEAD'])
def head_ta(task_tag,task_tag1):
     f=1
     with open('final.json') as f:
      data=json.load(f)     
     with open('type.json') as f1:
      types=json.load(f1) 
     for i in xrange(len(types)):    
      if types[i]==task_tag:
       f=0
       break
     if f:
      return make_response(jsonify({'no-content': 'false'}), 204)
     task=[task for task in data[task_tag] if task['name']==task_tag1]
     if not task:
       return make_response(jsonify({'no-content': 'false'}), 204)
     return jsonify({'Score-card':task})
     
@app.route('/sentiment/getall/<string:task_tag>/', methods=['HEAD'])
def head_t(task_tag):
     arr=[]
     with open('final.json') as f:
      data=json.load(f)   
     with open('type.json') as f1:
      types=json.load(f1) 
     for i in xrange(len(types)):  
      if types[i]: 
       task=[task for task in data[types[i]] if task['name']==task_tag]
       if task:
        arr.append(task)
     if not arr:
       return make_response(jsonify({'no-content': 'false'}), 204)
     return jsonify({'Score-card':arr})





@app.route('/sentiment/get/', methods=['GET'])
def get_task():
     with open('final.json') as f:
      data=json.load(f)     
     with open('type.json') as f1:
      types=json.load(f1) 
      if not data:
        return make_response(jsonify({'no-content': 'false'}), 204)
     return jsonify({'Score-card':data})

@app.route('/sentiment/get/<string:task_tag>/', methods=['GET'])
def get_tas(task_tag):
     with open('final.json') as f:
      data=json.load(f)     
     with open('type.json') as f1:
      types=json.load(f1) 
     for i in xrange(len(types)):    
      if types[i]==task_tag:
       return jsonify({'Score-card':data[task_tag]})    
     return make_response(jsonify({'no-content': 'false'}), 204)

@app.route('/sentiment/get/<string:task_tag>/<string:task_tag1>/', methods=['GET'])
def get_ta(task_tag,task_tag1):
     f=1
     with open('final.json') as f:
      data=json.load(f)     
     with open('type.json') as f1:
      types=json.load(f1) 
     for i in xrange(len(types)):    
      if types[i]==task_tag:
       f=0
       break
     if f:
      return make_response(jsonify({'no-content': 'false'}), 204)
     task=[task for task in data[task_tag] if task['name']==task_tag1]
     if not task:
       return make_response(jsonify({'no-content': 'false'}), 204)
     return jsonify({'Score-card':task})
     
@app.route('/sentiment/getall/<string:task_tag>/', methods=['GET'])
def get_t(task_tag):
     arr=[]
     with open('final.json') as f:
      data=json.load(f)   
     with open('type.json') as f1:
      types=json.load(f1) 
     for i in xrange(len(types)):  
      if types[i]: 
       task=[task for task in data[types[i]] if task['name']==task_tag]
       if task:
        arr.append(task)
     if not arr:
       return make_response(jsonify({'no-content': 'false'}), 204)
     return jsonify({'Score-card':arr})




 
@app.route('/sentiment/delete/', methods=['DELETE'])
def delete_task():
      with open('final.json') as f:
       data=json.load(f)
      with open('type.json') as f1:
       types=json.load(f1)  
      if not data:
        return make_response(jsonify({'no-content': 'false'}), 204)
      data={}
      types=[]
      open('final.json',"w").write(json.dumps(data))
      open('type.json',"w").write(json.dumps(types))
      return make_response(jsonify({'after-result': 'successfully deleted' }),200)

@app.route('/sentiment/delete/<string:task_tag>/', methods=['DELETE'])
def delete_tas(task_tag):
      f=1
      with open('final.json') as f:
       data=json.load(f) 
      with open('type.json') as f1:
       types=json.load(f1) 
      for i in xrange(len(types)):    
       if types[i]==task_tag:
        f=0
        break
      if f:
       return make_response(jsonify({'no-content': 'false'}), 204)
      data[task_tag]=[]
      for i in xrange(len(types)):
       if types[i]==task_tag:
         types.pop(i)
         break 
      open('final.json',"w").write(json.dumps(data))
      open('type.json',"w").write(json.dumps(types))
      return make_response(jsonify({'after-result': 'successfully deleted' }),200)

@app.route('/sentiment/delete/<string:task_tag>/<string:task_tag1>/', methods=['DELETE'])
def delete_ta(task_tag,task_tag1):
      with open('final.json') as f:
       data=json.load(f) 
      with open('type.json') as f1:
       types=json.load(f1) 
      for i in xrange(len(types)):    
       if types[i]==task_tag:
        f=0
        break
      if f:
       return make_response(jsonify({'no-content': 'false'}), 204)
      for i in xrange(len(data[task_tag])):
       if data[task_tag][i]['name']==task_tag1:
            task=data[task_tag][i]
      if not task:
       return make_response(jsonify({'no-content': 'false'}), 204) 
      data[task_tag].remove(task) 
      if not data[task_tag]:
       for i in xrange(len(types)):
        if types[i]==task_tag:
         types.pop(i)
         break
      open('final.json',"w").write(json.dumps(data))
      open('type.json',"w").write(json.dumps(types))
      return make_response(jsonify({'after-result': 'successfully deleted' }),200)

@app.route('/sentiment/deleteall/<string:task_tag>/', methods=['DELETE'])
def delete_t(task_tag):
      f=1
      with open('final.json') as f:
       data=json.load(f) 
      with open('type.json') as f1:
       types=json.load(f1) 
      if not data:
       return make_response(jsonify({'no-content': 'false'}), 204)  
      for i in xrange(len(types)): 
       for j in xrange(len(data[types[i]])):
        if data[types[i]][j]['name']==task_tag:
         data[types[i]].remove(data[types[i]][j])
         f=0
         break
       if not data[types[i]]:
        types.pop(i)
        break 
      if f:
       return make_response(jsonify({'no-content': 'false'}), 204)
      open('final.json',"w").write(json.dumps(data))
      open('type.json',"w").write(json.dumps(types))
      return make_response(jsonify({'after-result': 'successfully-deleted'}),200)





@app.route('/sentiment/post', methods=['POST'])
def post_task():
    f=0
    pp=0
    if not request.json:
        abort(400)
    with open('final.json') as f:
     data=json.load(f)
    with open('type.json') as f1:
     types=json.load(f1)
    if 'name' in request.json and type(request.json['name']) is not unicode:
     abort(400)
    if 'score' in request.json and type(request.json['score']) is unicode:
     abort(400)
    if 'type' in request.json and type(request.json['type']) is not unicode:
     abort(400)
    task = {
        'name': request.json['name'],
        'score': request.json['score'],
        'type': request.json['type']
       }
    for i in xrange(len(types)):
     if types[i]==task['type']:
      f=1
      for j in xrange(len(data[types[i]])):     
       if data[types[i]][j]['name']==task['name']:
        data[types[i]].remove(data[types[i]][j])
        data[types[i]].append(task)
        pp=1
        break
    if pp:   
     open('final.json',"w").write(json.dumps(data))
     return make_response(jsonify({task['type']:'updated-successfully'}), 200)
    if f==1 and pp==0:
     data[task['type']].append(task)
     open('final.json',"w").write(json.dumps(data))
     return make_response(jsonify({task['name']:'created successfully'}), 201)     
    data[task['type']]=[]
    data[task['type']].append(task)
    types.append(task['type'])
    open('final.json',"w").write(json.dumps(data))    
    open('type.json',"w").write(json.dumps(types))
    return make_response(jsonify({task['type']:'created'}),201) 
    




@app.route('/sentiment/put/<string:task_tag>', methods=['PUT'])
def put_task(task_tag):
   f=1
   ii=1
   with open('final.json') as f:
    data=json.load(f) 
   with open('type.json') as f1:
    types=json.load(f1)
   for i in xrange(len(types)):
    if types[i]==task_tag:
     f=0
   if f == 1:
    return make_response(jsonify({'no-content': 'false'}), 204)
   if not request.json:
    abort(400)
   if 'name' in request.json and type(request.json['name']) is not unicode:
    abort(400)
   if 'score' in request.json and type(request.json['score']) is unicode:
    abort(400)
   if 'type' in request.json and type(request.json['type']) is not unicode:
    abort(400)
   task = {
        'name': request.json['name'],
        'score': request.json['score'],
        'type': request.json['type']
    }
   if task['type']!=task_tag:
    return make_response(jsonify({'type':'invalid'}),400)
   for i in xrange(len(data[task_tag])):
    if data[task_tag][i]['name']==task['name']:
     ii=0   
     data[task_tag].remove(data[task_tag][i])
     data[task_tag].append(task)
     break
   if ii==1:
    return make_response(jsonify({'no-content': 'false'}), 204)
   open('final.json',"w").write(json.dumps(data))
   return make_response(jsonify({task['type']:'updated'}),200)





@app.route('/sentiment/patch', methods=['PATCH'])
def patch_task():
   f=1
   ii=1
   jj=1
   kk=1
   with open('final.json') as f:
    data=json.load(f) 
   with open('type.json') as f1:
    types=json.load(f1) 
   if not request.json:
        abort(400)
   if 'name' not in request.json:
        abort(400)
   if 'score' not in request.json:
        abort(400)
   if 'name' in request.json and type(request.json['name']) is not unicode:
    abort(400)
   if 'score' in request.json and type(request.json['score']) is unicode:
    abort(400)
   if 'type' in request.json and type(request.json['type']) is not unicode:
    abort(400)
   if 'type' in request.json:
    task = {
        'name': request.json['name'],
        'score': request.json['score'],
        'type': request.json['type']
     }
   if 'type' not in request.json:
    task = {
        'name': request.json['name'],
        'score': request.json['score'],
        'type': 'no'
      }  
   if task['type'] == 'no':
    for i in xrange(len(types)):
     for j in xrange(len(data[types[i]])):
      if data[types[i]][j]['name']==task['name']:
       data[types[i]][j]['score']=task['score']
       open('final.json',"w").write(json.dumps(data))
       ii=0
    if ii==1:
     return make_response(jsonify({'no-content': 'false'}), 204) 
    return jsonify({'contents':'updated'})
   for i in xrange(len(types)):
    if types[i]==task['type']:
     f=0
   if f==1:
       return make_response(jsonify({'no-content': 'false'}), 204)
   for i in xrange(len(data[task['type']])):
    if data[task['type']][i]['name']==task['name']:
     data[task['type']][i]['score']=task['score']
     kk=0
   if kk==1:   
    return make_response(jsonify({'no-content': 'false'}), 204)
   open('final.json',"w").write(json.dumps(data))
   return jsonify({'contents':'updated'})





@app.route('/sentiment/propfind/<string:task_tag>', methods=['PROPFIND'])
def propfind_task(task_tag):
   tasks=[]
   with open('final.json') as f:
    data=json.load(f)
   with open('type.json') as f1:
    types=json.load(f1) 
   if len(data) == 0:
    return make_response(jsonify({'no-content': 'false'}), 204)
   if task_tag == 'type':
    for i in xrange(len(types)):
     tasks.append(types[i])     
    return make_response(jsonify({'types': tasks}), 200)
   if task_tag == 'name': 
    for i in xrange(len(types)):
     if types[i]:
      for j in xrange(len(data[types[i]])):
       tasks.append(data[types[i]][j]['name'])
    return make_response(jsonify({'names': tasks}), 200)
   if task_tag == 'score': 
    for i in xrange(len(types)):
     if types[i]:
      for j in xrange(len(data[types[i]])):
       tasks.append(data[types[i]][j]['score'])
    return make_response(jsonify({'scores': tasks}), 200)
   return make_response(jsonify({'Invalid': 'request'}), 400)
   




@app.route('/sentiment/copy/<string:fromm>/<string:what>/<string:to>', methods=['COPY'])
def copy_task(fromm,what,to):
   ii=1
   jj=1
   f=1
   with open('final.json') as f:
    data=json.load(f)
   with open('type.json') as f1:
    types=json.load(f1) 
   for i in xrange(len(types)):
    if types[i]==fromm:
     ii=0
    if types[i]==to:
     jj=0 
   if ii==0 and jj==0:
    for i in xrange(len(data[fromm])):
     if data[fromm][i]['name']==what:
      task={
           'name':what,
           'score':data[fromm][i]['score'],
           'type':to
           }
      for j in xrange(len(data[to])):
       if data[to][j]['name']==what:
        data[to][j]['score']=task['score']
        open('final.json',"w").write(json.dumps(data))
        return make_response(jsonify({'updated': 'successfully'}), 200)
      data[to].append(task)
      open('final.json',"w").write(json.dumps(data))
      return make_response(jsonify({'copied': 'successfully'}), 200)
   if ii==0 and jj==1:
    types.append(to)
    open('type.json',"w").write(json.dumps(types))
    for i in xrange(len(data[fromm])):
     if data[fromm][i]['name']==what:
      task={
           'name':what,
           'score':data[fromm][i]['score'],
           'type':to
           }
      data[to].append(task)      
      open('final.json',"w").write(json.dumps(data))
      return make_response(jsonify({'copied': 'successfully'}), 200)
   return make_response(jsonify({'information': 'false'}), 204) 





@app.route('/sentiment/move/<string:fromm>/<string:what>/<string:to>', methods=['MOVE'])
def move_task(fromm,what,to):
   ii=1
   jj=1
   f=1
   with open('final.json') as f:
    data=json.load(f)
   with open('type.json') as f1:
    types=json.load(f1) 
   for i in xrange(len(types)):
    if types[i]==fromm:
     ii=0
    if types[i]==to:
     jj=0 
   if ii==0 and jj==0:
    for i in xrange(len(data[fromm])):
     if data[fromm][i]['name']==what:
      task={
           'name':what,
           'score':data[fromm][i]['score'],
           'type':to
           }
      for j in xrange(len(data[to])): 
       if data[to][j]['name']==what:
        data[to][j]['score']=task['score']
        data[fromm].remove(data[fromm][i])
        if not data[fromm]:
         for i in xrange(len(types)):
          if types[i]==fromm:
           types.pop(i)
           open('type.json',"w").write(json.dumps(types))
           break
        open('final.json',"w").write(json.dumps(data))
        return make_response(jsonify({'updated': 'successfully'}), 200)
      data[to].append(task)
      data[fromm].remove(data[fromm][i])
      if not data[fromm]:
       for i in xrange(len(types)):
        if types[i]==fromm:
         types.pop(i)
         open('type.json',"w").write(json.dumps(types))
         break
      open('final.json',"w").write(json.dumps(data))
      return make_response(jsonify({'moved': 'successfully'}), 200)
   if ii==0 and jj==1:
    types.append(to)
    open('type.json',"w").write(json.dumps(types))
    for i in xrange(len(data[fromm])):
     if data[fromm][i]['name']==what:
      task={
           'name':what,
           'score':data[fromm][i]['score'],
           'type':to
           }
      data[to].append(task)
      open('final.json',"w").write(json.dumps(data))
      return make_response(jsonify({'moved': 'successfully'}), 200)
   return make_response(jsonify({'information': 'false'}), 204) 





@app.route('/sentiment/options', methods=['OPTIONS'])
def option_task():
   task={
         'GET/':'List all Entries', 
         'GET':'List specific entries',
         'HEAD':'Display header',
         'DELETE':'Delete specific entry',
         'POST':'Add the new entry',
         'PUT':'Update the entry',
         'PATCH':'Update only the listed sub entry',
         'PROPFIND':'List all details of specific category',
         'OPTIONS':'List all operations',
         'COPY':'Copy of one type sub entry to other type',
         'MOVE':'Move entry of one type to other'
         }
   return make_response(jsonify({'OPERATIONS': task}),200)





@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not found'}),404)

if __name__ == '__main__':
  app.run(debug=True)
