import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    LOCAL_FILE_NAME = '/tmp/downloaded.txt'
    print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    response = s3.get_object(Bucket=bucket, Key=key)
    s3.download_file(bucket, key, LOCAL_FILE_NAME)
    f = open('/tmp/downloaded.txt')
    lines = f.readlines()
    print(lines)
    list4=[]
    list4=lines
    print(list4)
    print(list4[8])
    f.close()
    def sem1():
        list=[]
        m1=list4[3]
        m1=int(m1)//10+1
        list.append(m1)
        m2=list4[4]
        m2=int(m2)//10+1
        list.append(m2)
        m3=list4[5]
        m3=int(m3)//10+1
        list.append(m3)
        m4=list4[6]
        m4=int(m4)//10+1
        list.append(m4)
        m5=list4[7]
        m5=int(m5)//10+1
        list.append(m5)
        m6=list4[8]
        m6=int(m6)//10+1
        list.append(m6)
        m7=list4[9]
        m7=int(m7)//10+1
        list.append(m7)
        m8=list4[10]
        m8=int(m8)//10+1
        list.append(m8)
        print(list)
        list1=[4,4,3,3,3,1,1,1]
        result=[]
        for i in range(0,len(list),1):
            k=list1[i]*list[i]
            result.append(k)
        print(result)
        total=sum(result)
        sgpa=total/sum(list1)
        print(sgpa)
        
        G=[]
        
        x=sgpa
        if (x>=7.75) :
            G.append("Distinction")
        if x >=6 and x< 7.5 :
            G.append("First class")
        if x >=5 and x<6:
            G.append("Second class")
        
        sgpa=str(sgpa)
      
        G.append(sgpa)
        # ---------DYNAMODB-----------------
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('project')
        response=table.put_item(
            
        Item={
            'usn':list4[0],
            'name':list4[1],
            'sem':list4[2],
            'sgpa':G[1],
            'Class':G[0]
             }
        )
        # ---------DYNAMODB-----------------
        
        
        
    def sem2():
        list=[]
        m1=list4[3]
        m1=int(m1)//10+1
        list.append(m1)
        m2=list4[4]
        m2=int(m2)//10+1
        list.append(m2)
        m3=list4[5]
        m3=int(m3)//10+1
        list.append(m3)
        m4=list4[6]
        m4=int(m4)//10+1
        list.append(m4)
        m5=list4[7]
        m5=int(m5)//10+1
        list.append(m5)
        m6=list4[8]
        m6=int(m6)//10+1
        list.append(m6)
        m7=list4[9]
        m7=int(m7)//10+1
        list.append(m7)
        m8=list4[10]
        m8=int(m8)//10+1
        list.append(m8)
        print(list)
        list1=[4,4,3,3,3,1,1,1]
        result=[]
        for i in range(0,len(list),1):
            k=list1[i]*list[i]
            result.append(k)
        print(result)
        total=sum(result)
        sgpa=total/sum(list1)
        print(sgpa)
        G=[]
        
        x=sgpa
        if (x>=7.75) :
            G.append("Distinction")
        if x >=6 and x< 7.5 :
            G.append("First class")
        if x >=5 and x<6:
            G.append("Second class")
        
        sgpa=str(sgpa)
      
        G.append(sgpa)
        # ---------DYNAMODB-----------------
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('project')
        response=table.put_item(
            
        Item={
            'usn':list4[0],
            'name':list4[1],
            'sem':list4[2],
            'sgpa':G[1],
            'Class':G[0]
             }
        )
        # ---------DYNAMODB-----------------
        
        
        
        
    def sem3():
        list=[]
        m1=list4[3]
        m1=int(m1)//10+1
        list.append(m1)
        m2=list4[4]
        m2=int(m2)//10+1
        list.append(m2)
        m3=list4[5]
        m3=int(m3)//10+1
        list.append(m3)
        m4=list4[6]
        m4=int(m4)//10+1
        list.append(m4)
        m5=list4[7]
        m5=int(m5)//10+1
        list.append(m5)
        m6=list4[8]
        m6=int(m6)//10+1
        list.append(m6)
        m7=list4[9]
        m7=int(m7)//10+1
        list.append(m7)
        m8=list4[10]
        m8=int(m8)//10+1
        list.append(m8)
        m9=list4[11]
        m9=int(m9)//10+1
        list.append(m9)
        print(list)
        list1=[3,4,3,3,3,3,2,2,1]
        result=[]
        for i in range(0,len(list),1):
            k=list1[i]*list[i]
            result.append(k)
        print(result)
        total=sum(result)
        sgpa=total/sum(list1)
        print(sgpa)
        G=[]
        
        x=sgpa
        if (x>=7.75) :
            G.append("Distinction")
        if x >=6 and x< 7.5 :
            G.append("First class")
        if x >=5 and x<6:
            G.append("Second class")
        
        sgpa=str(sgpa)
      
        G.append(sgpa)
        # ---------DYNAMODB-----------------
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('project')
        response=table.put_item(
            
        Item={
            'usn':list4[0],
            'name':list4[1],
            'sem':list4[2],
            'sgpa':G[1],
            'Class':G[0]
             }
        )
        # ---------DYNAMODB-----------------
        
        
        
        
        
    def sem4():
        list=[]
        m1=list4[3]
        m1=int(m1)//10+1
        list.append(m1)
        m2=list4[4]
        m2=int(m2)//10+1
        list.append(m2)
        m3=list4[5]
        m3=int(m3)//10+1
        list.append(m3)
        m4=list4[6]
        m4=int(m4)//10+1
        list.append(m4)
        m5=list4[7]
        m5=int(m5)//10+1
        list.append(m5)
        m6=list4[8]
        m6=int(m6)//10+1
        list.append(m6)
        m7=list4[9]
        m7=int(m7)//10+1
        list.append(m7)
        m8=list4[10]
        m8=int(m8)//10+1
        list.append(m8)
        m9=list4[11]
        m9=int(m9)//10+1
        list.append(m9)
        print(list)
        list1=[3,4,3,3,3,3,2,2,1]
        result=[]
        for i in range(0,len(list),1):
            k=list1[i]*list[i]
            result.append(k)
        print(result)
        total=sum(result)
        sgpa=total/sum(list1)
        print(sgpa)
        G=[]
        
        x=sgpa
        if (x>=7.75) :
            G.append("Distinction")
        if x >=6 and x< 7.5 :
            G.append("First class")
        if x >=5 and x<6:
            G.append("Second class")
        
        sgpa=str(sgpa)
      
        G.append(sgpa)
        # ---------DYNAMODB-----------------
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('project')
        response=table.put_item(
            
        Item={
            'usn':list4[0],
            'name':list4[1],
            'sem':list4[2],
            'sgpa':G[1],
            'Class':G[0]
             }
        )
        # ---------DYNAMODB-----------------
        
        
        
    def sem5():
        list=[]
        m1=list4[3]
        m1=int(m1)//10+1
        list.append(m1)
        m2=list4[4]
        m2=int(m2)//10+1
        list.append(m2)
        m3=list4[5]
        m3=int(m3)//10+1
        list.append(m3)
        m4=list4[6]
        m4=int(m4)//10+1
        list.append(m4)
        m5=list4[7]
        m5=int(m5)//10+1
        list.append(m5)
        m6=list4[8]
        m6=int(m6)//10+1
        list.append(m6)
        m7=list4[9]
        m7=int(m7)//10+1
        list.append(m7)
        m8=list4[10]
        m8=int(m8)//10+1
        list.append(m8)
        m9=list4[11]
        m9=int(m9)//10+1
        list.append(m9)
        print(list)
        list1=[3,4,4,3,3,3,2,2,1]
        result=[]
        for i in range(0,len(list),1):
            k=list1[i]*list[i]
            result.append(k)
        print(result)
        total=sum(result)
        sgpa=total/sum(list1)
        print(sgpa)
        G=[]
        
        x=sgpa
        if (x>=7.75) :
            G.append("Distinction")
        if x >=6 and x< 7.5 :
            G.append("First class")
        if x >=5 and x<6:
            G.append("Second class")
        
        sgpa=str(sgpa)
      
        G.append(sgpa)
        # ---------DYNAMODB-----------------
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('project')
        response=table.put_item(
            
        Item={
            'usn':list4[0],
            'name':list4[1],
            'sem':list4[2],
            'sgpa':G[1],
            'Class':G[0]
             }
        )
        # ---------DYNAMODB-----------------
        
        
        
        
    def sem6():
        list=[]
        m1=list4[3]
        m1=int(m1)//10+1
        list.append(m1)
        m2=list4[4]
        m2=int(m2)//10+1
        list.append(m2)
        m3=list4[5]
        m3=int(m3)//10+1
        list.append(m3)
        m4=list4[6]
        m4=int(m4)//10+1
        list.append(m4)
        m5=list4[7]
        m5=int(m5)//10+1
        list.append(m5)
        m6=list4[8]
        m6=int(m6)//10+1
        list.append(m6)
        m7=list4[9]
        m7=int(m7)//10+1
        list.append(m7)
        m8=list4[10]
        m8=int(m8)//10+1
        list.append(m8)
        print(list)
        list1=[4,4,4,3,3,2,2,2]
        result=[]
        for i in range(0,len(list),1):
            k=list1[i]*list[i]
            result.append(k)
        print(result)
        total=sum(result)
        sgpa=total/sum(list1)
        print(sgpa)
        G=[]
        
        x=sgpa
        if (x>=7.75) :
            G.append("Distinction")
        if x >=6 and x< 7.5 :
            G.append("First class")
        if x >=5 and x<6:
            G.append("Second class")
        
        sgpa=str(sgpa)
      
        G.append(sgpa)
        # ---------DYNAMODB-----------------
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('project')
        response=table.put_item(
            
        Item={
            'usn':list4[0],
            'name':list4[1],
            'sem':list4[2],
            'sgpa':G[1],
            'Class':G[0]
             }
        )
        # ---------DYNAMODB-----------------
    k=list4[2]
    f=int(k)

    if   (f==1):
        sem1()
    elif (f==2):
        sem2()
    elif (f==3):
        sem3()
    elif (f==4):
        sem4()
    elif (f==5):
        sem5()
    elif (f==6):
        sem6()

    return {
         'statusCode': 200,
          'body': json.dumps('Hello from Lambda!')
        }

              
