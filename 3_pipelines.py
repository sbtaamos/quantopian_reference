# Pipeline class
from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.psychsignal import stocktwits
from quantopian.pipeline.data import USEquityPricing

from quantopian.pipeline.factors import SimpleMovingAverage

def make_pipeline():
    # Get latest closing price
    close_price = USEquityPricing.close.latest

    # Calculate 3 day average of bull_minus_bear scores
    sentiment_score = SimpleMovingAverage(
        inputs=[stocktwits.bull_minus_bear],
        window_length=3,
    )
    # Return Pipeline containing close_price
    # and sentiment_score
    return Pipeline(
        columns={
            'close_price': close_price,
            'sentiment_score': sentiment_score,
        }
    )

