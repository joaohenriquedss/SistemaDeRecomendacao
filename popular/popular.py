#Recomendando o que é Popular
from collections import Counter

users_interests = [
  ['Hadoop','Big Data','HBase','Java','Spark','Storm','Cassandra'],
  ['NoSQL','MongoDB','Cassandra','HBase','Postgres'],
  ['Python','scikit-learn','scipy','numpy','statsmodels','pandas'],
  ['R','Python','statistics','regression','probability'],
  ['machine learning','regression','decision trees','libsvm'],
  ['Python','R','Java','C++','Haskell','programming languages'],
  ['statistics','probability','mathematics','theory'],
  ['machine learning','scikit-learn','Mahout','neural networks'],
  ['neural networks','deep learning','Big Data','artificial intelligence'],
  ['Hadoop','Java','MapReduce','Big Data'],
  ['statistics','R','statsmodels'],
  ['C++','deep learning','artificial intelligence','probability'],
  ['pandas','R','Python'],
  ['database','HBase','Postgres','MySQL','MongoDB'],
  ['libsvm','regression','support vector machines']
]

popular_interests = Counter(interest
                            for user_interests in users_interests
                            for interest in user_interests).most_common()

#print(popular_interests)

# Tendo computado isso,podemos apenas sugerir a um usuário os interesses mais populares pelas quais ele ainda não esta interessado
def top_popular(user_interests, max_results=5):
  suggestions = [(interest,frequency)
                for interest, frequency in popular_interests
                if interest not in user_interests]
  return suggestions[:max_results]

print('-'*30)
print(top_popular(users_interests[3],5))

