# Stock Ranking ML (US Equities)

## Goal
Benchmark multiple ML model families (linear, probabilistic, tree-based, boosting, and later deep learning) for **cross-sectional stock ranking**.

## Task
Given features up to date *t*, predict a score to rank stocks by **5-day forward performance** (long-only evaluation).

## Validation
We use **nested time-series cross-validation** (walk-forward) with **date-grouped splits** to avoid leakage. Standard random K-fold is not used.

## Metrics
- Spearman IC (rank correlation)
- Precision@K (top-K overlap)
- Decile spread (top minus bottom decile forward return)
- Secondary: MSE (on transformed labels)

## Roadmap
Phase 1: Momentum baseline, Ridge, Random Forest, XGBoost  
Phase 2: Logistic, Naive Bayes, Decision Tree, XGBoost ranking objective  
Phase 3: MLP, CNN, LSTM/GRU (sequential track)
