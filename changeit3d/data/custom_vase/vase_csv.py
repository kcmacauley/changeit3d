import pandas as pd
from changeit3d.language.vocabulary import Vocabulary

vocab = Vocabulary.load('/home/kcmacauley/changeit3d/changeit3d/data/shapetalk/language/vocabulary.pkl')
# Define the DataFrame with the provided data
data = {
    'workerid': ['user_9999'],
    'utterance': ['The target is less jagged'],
    'assignmentid': ['assignment_0'],
    'worktimeinseconds': [200],
    'source_model_name': ['vase_0288'],
    'source_object_class': ['vase'],
    'source_dataset': ['CustomVase'],
    'target_model_name': ['vase/vase_0288.npz'],
    'target_object_class': ['vase'],
    'target_dataset': ['ModelNet'],
    'is_patched': [False],
    'target_uid': ['vase/vase_0288.npz'],
    'source_uid': ['vase/vase_0288.npz'],
    'hard_context': [True],
    'target_original_object_class': ['vase'],
    'source_original_object_class': ['vase'],
    'saliency': [0],
    'tokens': [["the", "target", "is", "less", "jagged"]],
    'tokens_len': [5],
    'utterance_spelled': ['The target is less jagged'],
    'target_unary_split': ['test'],
    'source_unary_split': ['test'],
    'listening_split': ['test'],
    'changeit_split': ['test'],
    'tokens_encoded': [[1, 10, 11, 7, 229, 1427, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
}


# Create the DataFrame
df = pd.DataFrame(data)
utter = ['the base is round and closed', "the target is less jagged", "the target is filled in", "the target has no holes", "the target is taller"]

# Create additional rows using a for loop
for i in range(5):
    ndf_temp = df.iloc[0].copy()  # Copy the first row
    ndf_temp['workerid'] = f'user_999{i}'
    ndf_temp['assignmentid'] = f'5G7J3D9R2T6F1A8K0L4S2Q9P6H5J{i}D'
    ndf_temp['utterance'] = utter[i]
    ndf_temp['utterance_spelled'] = ndf_temp['utterance']
    ndf_temp['tokens'] = ndf_temp['utterance'].split()
    ndf_temp['source_model_name'] = f'vase_0{i+1}.npz'
    ndf_temp['source_uid'] = f'vase/vase_0{i+1}.npz'
    # ndf_temp['distractor_1'] = f'vase_0{i+1}.npz'

    max_len = max(df['tokens'].apply(len).max(), len(ndf_temp['tokens']))
    # Append the row to the DataFrame
    df = df.append(ndf_temp, ignore_index=True)

df['tokens_encoded'] = df['tokens'].apply(lambda x: vocab.encode(x, max_len=max_len))
df = df.drop(df.index[0])

# Display the DataFrame
print(df)
df.to_csv('custom_vase.csv', index=False)

