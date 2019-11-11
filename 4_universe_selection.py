# Import Pipeline class and datasets
from quantopian.pipeline import Pipeline
from quantopian.research import run_pipeline
from quantopian.pipeline.data import USEquityPricing
from quantopian.pipeline.data.psychsignal import stocktwits

# Import built-in moving average calculation
from quantopian.pipeline.factors import SimpleMovingAverage

# Import built-in trading universe
from quantopian.pipeline.filters import QTradableStocksUS

def make_pipeline():
    # Create a reference to our trading universe
    base_universe = QTradableStocksUS()

    # get latest closing price
    close_price = USEquityPricing.close.latest

    # calculate 3 day MA of bull-minus-bear scores
    sentiment_score = SimpleMovingAverage(
        inputs=[stocktwits.bull_minus_bear],
        window_length=3,
    )

    # Return Pipeline containing close_price and sentiment_score
    return Pipeline(
        columns={'close_price': close_price,
                 'sentiment_score': sentiment_score,
        }
        screen=base_universe
    )

## Execute the Pipeline
pipeline_output = run_pipeline(
    make_pipeline(),
    start_date='2013-01-01',
    end_date='2013-12-31'
)

# Display last 10 rows
pipeline_output.tail(10)
