import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import polars as pl
    from lets_plot import ggplot, aes, geom_point, theme_minimal2

    return (pl,)


@app.cell
def _(pl):
    # importing the data for EDA
    data = pl.read_parquet('output/pp_2020-2026.parquet')
    data.head()
    return (data,)


@app.cell
def _(data_interest, pl):
    ## split the barcode with the first 3 digits and the last 3 digits
    split_postcode_data = (
        data_interest
        .with_columns(
            pl.col('postcode')
                .str.to_lowercase()
                .str.split_exact(' ', 1)
                .struct
                .rename_fields(['postcode_first', 'postcode_last'])
                .alias('postcode_split')
        )
        .unnest('postcode_split')
    )
    return


@app.cell
def _():
    ## annotate th city of interest into the original dataframe instead of filetering them out
    city_of_interest = [
        'CAMBRIDGE',
        'ROYSTON',
        'SAFFRON WALDEN',
        'STEVENAGE'
    ]
    return


@app.cell
def _(data, pl):
    ## the cities that I am interested
    city_of_interest = [
        'CAMBRIDGE',
        'ROYSTON',
        'SAFFRON WALDEN',
        'STEVENAGE'
    ]

    ## filter these cities out
    data_interest = (
        data
        .filter(
            pl.col('town_city').is_in(city_of_interest)
        )
    )

    print(f'data shape: {data_interest.shape}')
    data_interest.head()
    return (data_interest,)


@app.cell
def _(data_interest, pl):
    ## split the postcode into first 3 digits and last 3 digits
    data_postcodes = (
        data_interest
        .with_columns(
            pl.col('postcode')
                .str.to_lowercase()
                .str.split_exact(' ', 1)
                .struct
                .rename_fields(['postcode_first', 'postcode_last'])
                .alias('postcode_split')
        )
        .unnest('postcode_split')
        .drop('postcode')
    )


    return


if __name__ == "__main__":
    app.run()
