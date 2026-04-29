# Black-Scholes Pricing Model

A Python-based implementation of the Black-Scholes options pricing model with an interactive Streamlit dashboard.

## Overview

This project calculates theoretical Call and Put option prices using the Black-Scholes model and visualizes them in an interactive web dashboard. Users can adjust key financial parameters in real time and observe how they affect option prices and the pricing heatmap.

## Features

- Real-time calculation of Call and Put option prices
- Interactive heatmap showing option prices across a range of spot prices and volatilities
- Adjustable parameters via a sidebar with sliders and input fields
- Clean dashboard built with Streamlit and Seaborn

## Project Structure

- black_scholes_formula.py - Core Black-Scholes formula implementation
- black_scholes_visualization.py - Heatmap data generation and plotting functions
- black_scholes_streamlit.py - Streamlit dashboard application

## Parameters

- Current Asset Price - The current market price of the underlying asset
- Strike Price - The agreed price at which the option can be exercised
- Time to Maturity - Time until the option expires, in years
- Volatility - Expected price fluctuation of the underlying asset
- Risk-Free Interest Rate - The theoretical return of a risk-free investment

## Installation

pip install streamlit seaborn matplotlib numpy scipy

## Usage

streamlit run black_scholes_streamlit.py

## How It Works

The Black-Scholes model calculates the fair price of a European option based on five inputs. The formula uses the cumulative normal distribution to estimate the probability that an option will expire in the money, discounted by the risk-free rate over the remaining time to maturity.
