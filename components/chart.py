import streamlit as st


def chart(symbol: str):
    # Dynamic input for TradingView symbol
    st.markdown("## Live Stock Chart")

    # TradingView chart embed with dynamic symbol
    st.components.v1.html(
        f"""
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
            <div id="tradingview_chart"></div>
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">
            new TradingView.widget(
            {{
                "width": 600,
                "height": 300,
                "symbol": "{symbol}",  // Dynamically set the symbol here
                "interval": "D",
                "timezone": "Etc/UTC",
                "theme": "light",
                "style": "1",
                "locale": "en",
                "toolbar_bg": "#f1f3f6",
                "enable_publishing": false,
                "withdateranges": true,
                "range": "YTD",
                "hide_side_toolbar": false,
                "allow_symbol_change": true,
                "container_id": "tradingview_chart"
            }}
            );
            </script>
        </div>
        <!-- TradingView Widget END -->
        """,
        height=300
    )
