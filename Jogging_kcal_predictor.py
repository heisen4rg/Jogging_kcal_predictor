#This is based on MET (Metabolic Equivalent of Task) value for jogging at 9 km/h, which is roughly 9.8 METs.
#The kcal burnt displayed is for a person weighing 70kgs and jogging at an avg pace of 9kpmh.
def compute(w,b): #calculating the prediction linear line f(x)=wx+b
    return[(w*x_data[i])+b for i in range(m)]
def cost_func(y_pred): #determines how accurate the model is predicting the output, lower the cost function the more accurate
    j=0
    for i in range(m):
        j1=((y_pred[i])-(y_data[i]))**2
        j+=j1
    j/=(2*m)
    return j
def grad_des(w, b, alpha): #brings the cost function down slowly for some w and b values
    dj_dw=0
    dj_db=0
    for i in range(m):
        djdw=x_data[i]*((y_pred[i])-(y_data[i]))
        dj_dw+=djdw
        djdb=((y_pred[i])-(y_data[i]))
        dj_db+=djdb
    dj_dw/=m
    dj_db/=m
    w-=(alpha*dj_dw)
    b-=(alpha*dj_db)
    return w, b
def predict(minutes, w, b):
    print(w*minutes+b,"kcal burnt")
x_data = [j for j in range(1, 61)]
y_data = [j * 11 for j in x_data]
m=len(y_data)
w = 25
b = 5
alpha = 0.001 
for epoch in range(10001):  # run for 10000 iterations
    y_pred=compute(w, b)
    w, b = grad_des(w, b, alpha)
    cost = cost_func(y_pred)
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}: w={w}, b={b}, cost={cost}")
    if cost > 1e6:
        print(f"Early stop at epoch {epoch}, cost too high: {cost}")
        break
w1, b1=w, b
try:
    x=int(input("how many minutes worked out?: "))
    y=int(input("how many seconds worked out?: "))
    time_worked_out=x+(y/60)
    predict(time_worked_out, w1, b1)
except ValueError:
    print("Invalid input. Please enter numbers only.")

