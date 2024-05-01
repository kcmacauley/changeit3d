import pandas as pd

df_source_data = pd.read_csv("shapetalk_preprocessed_filtered_for_shape_removal.csv")

columns = ['model_uid', 'object_class', 'dataset', 'model_name', 'split']

# Create an empty DataFrame with the specified columns
df_target_data = pd.DataFrame(columns=columns)
df_target_temp = pd.DataFrame(columns=columns)

# Display the empty DataFrame
df_target_data['model_uid'] = df_source_data['target_uid']
df_target_data['object_class'] = df_source_data['target_object_class']
df_target_data['dataset'] = df_source_data['target_dataset']
df_target_data['model_name'] = df_source_data['target_model_name']
df_target_data['split'] = df_source_data['changeit_split']
df_target_data = df_target_data.drop_duplicates(subset=['model_uid'])

df_target_temp['model_uid'] = df_source_data['source_uid']
df_target_temp['object_class'] = df_source_data['source_object_class']
df_target_temp['dataset'] = df_source_data['source_dataset']
df_target_temp['model_name'] = df_source_data['source_model_name']
df_target_temp['split'] = df_source_data['changeit_split']
df_target_temp = df_target_temp.drop_duplicates(subset=['model_uid'])

df_target_data = pd.concat([df_target_data, df_target_temp], ignore_index=True)

df_target_data.to_csv('seg_pc_ae_data.csv', index=False)
