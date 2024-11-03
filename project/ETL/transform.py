import pandas as pd

class Transformer:
    def __init__(self):
        self.unemployment_df = None
        self.crime_df = None

    def transform_data_delete_null(self):
        # Load data
        unemployment_pre = pd.read_csv(r"D:\\Github\\made-ws24\\data\\API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_10162.csv", skiprows=3)
        crime_pre = pd.read_csv(r"D:\\Github\\made-ws24\\data\\API_VC.IHR.PSRC.P5_DS2_en_csv_v2_20172.csv", skiprows=3)

        # Drop columns with null values (if they exist)
        columns_to_drop = [
            '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
            '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
            '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
            '1987', '1988', '1989', '1990', '2022', 'Unnamed: 67'
        ]

        unemployment_pre.drop(columns=[col for col in columns_to_drop if col in unemployment_pre.columns], inplace=True, errors='ignore')
        unemployment_pre.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'], inplace=True, errors='ignore')

        unemployment_pre.dropna(how='all', subset=unemployment_pre.columns[unemployment_pre.columns.get_loc('1991'):], inplace=True)

        crime_pre.drop(columns=[col for col in columns_to_drop if col in crime_pre.columns], inplace=True, errors='ignore')
        crime_pre.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'], inplace=True, errors='ignore')

        # Convert columns from 1991 onwards to numeric, coercing errors to NaN
        crime_pre.loc[:, '1991':] = crime_pre.loc[:, '1991':].apply(pd.to_numeric, errors='coerce')

        # Identify rows with more than 5 NaN values in numeric columns (from 1991 onwards)
        numeric_crime_data = crime_pre.loc[:, '1991':]
        countries_with_nulls = numeric_crime_data.isna().sum(axis=1) > 5

        # Drop rows where NaN values exceed 6
        crime_pre_cleaned = crime_pre[~countries_with_nulls]

        # Fill NaN values in numeric columns with their mean
        crime_pre_cleaned[numeric_crime_data.columns] = crime_pre_cleaned[numeric_crime_data.columns].fillna(crime_pre_cleaned[numeric_crime_data.columns].mean())
        unemployment_pre_cleaned = unemployment_pre.fillna(unemployment_pre.mean(numeric_only=True))

        return crime_pre_cleaned, unemployment_pre_cleaned

    def sync_both_data(self):
        self.crime_df, self.unemployment_df = self.transform_data_delete_null()
        remaining_countries = self.crime_df['Country Name'].tolist()
        unemployment_remaining_countries = self.unemployment_df[self.unemployment_df['Country Name'].isin(remaining_countries)]

        crime_skim = self.crime_df.set_index('Country Name').T
        to_remove = [
            'Bermuda', 'Cayman Islands', 'Faroe Islands', 'Micronesia, Fed. Sts.', 'Gibraltar',
            'Not classified', 'Liechtenstein', 'Monaco', 'Northern Mariana Islands', 'Nauru',
            'San Marino', 'Sint Maarten (Dutch part)'
        ]
        crime_skim.drop(columns=[col for col in to_remove if col in crime_skim.columns], inplace=True, errors='ignore')
        
        crime_final = crime_skim.T.reset_index()
        unemployment_final = unemployment_remaining_countries.reset_index(drop=True)

        return crime_final, unemployment_final

    def get_unemployment_data_not_null(self):
        return self.transform_data_delete_null()[1]

    def get_crime_data_not_null(self):
        return self.transform_data_delete_null()[0]

    def get_unemployment_data(self):
        return self.sync_both_data()[1]

    def get_crime_data(self):
        return self.sync_both_data()[0]
