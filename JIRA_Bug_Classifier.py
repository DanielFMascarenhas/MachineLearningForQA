import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split


df = pd.read_csv('bug_dataset_50k.csv')

df.columns()
#  let's assume title, bug_domain, environment are inputs
#  bug_category, developer_role, severity are possible outputs for bug classification.
#  In this model we will focus on bug_category

# Lets drop irrelevant columns
df.drop(['bug_id','description', 'error_code','tech_stack','root_cause','suggested_fix','explanation','created_at'], axis=1, inplace=True)

# convert categorical values into numerics
df['bug_domain_id'] = pd.factorize(df['bug_domain'])[0]
df['bug_category_id'] = pd.factorize(df['bug_category'])[0]
df['developer_role_id'] = pd.factorize(df['developer_role'])[0]
df['severity_id'] = pd.factorize(df['severity'])[0]
df['environment_id'] = pd.factorize(df['environment'])[0]

# Convert title into vectorized data
v = CountVectorizer()
df_x_title = v.fit_transform(df['title'])
df_x_title = pd.DataFrame(df_x_title.toarray())

# Now create final X & Y vectors
df_X = pd.concat([df_x_title,df[['bug_domain_id','environment_id']]],axis=1)
df_X.columns = df_X.columns.astype(str)

df_dev_role_Y = pd.concat([df[['developer_role_id']]],axis=1)
df_severity_Y = pd.concat([df[['severity_id']]],axis=1)
df_bug_category_Y = pd.concat([df[['bug_category_id']]],axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(df_X,df_bug_category_Y,test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train,Y_train)
print("final model score: ",model.score(X_test,Y_test))

