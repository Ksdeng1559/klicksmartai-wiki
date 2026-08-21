# LeadSniper BigQuery Analytics

BigQuery data warehouse for LeadSniper analytics, providing business intelligence and reporting capabilities.

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│    Supabase     │────▶│   ETL Pipeline  │────▶│    BigQuery     │
│  (Operational)  │     │ (Cloud Function)│     │   (Analytics)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                              │                         │
                              ▼                         ▼
                        ┌───────────┐           ┌──────────────┐
                        │ Scheduled │           │  Dashboards  │
                        │  Trigger  │           │  & Reports   │
                        └───────────┘           └──────────────┘
```

## Schema Overview

### Fact Tables (Event Data)
| Table | Description | Partition | Cluster |
|-------|-------------|-----------|---------|
| `fact_lead_searches` | Search events | `partition_date` | `niche, city` |
| `fact_lead_enrichments` | Enrichment events | `partition_date` | `source, enrichment_type` |
| `fact_content_generations` | AI content events | `partition_date` | `content_type, model_used` |
| `fact_seo_audits` | SEO audit events | `partition_date` | `data_source` |
| `fact_user_actions` | User interaction events | `partition_date` | `action_type, user_id` |
| `fact_exports` | Export events | `partition_date` | - |

### Dimension Tables (Reference Data)
| Table | Description | SCD Type |
|-------|-------------|----------|
| `dim_leads` | Lead master data | Type 2 |
| `dim_users` | User profiles | Type 1 |
| `dim_niches` | Niche reference | Type 1 |
| `dim_locations` | Geographic reference | Type 1 |
| `dim_campaigns` | Campaign reference | Type 1 |
| `dim_date` | Calendar dimension | Static |
| `dim_enrichment_sources` | API source reference | Type 1 |

### Aggregate Tables (Pre-Computed)
| Table | Description | Refresh |
|-------|-------------|---------|
| `agg_daily_metrics` | Daily KPIs | Daily |
| `agg_niche_performance` | Niche-level metrics | Daily |
| `agg_campaign_performance` | Campaign metrics | Daily |
| `agg_enrichment_performance` | API source metrics | Daily |
| `agg_weekly_trends` | Weekly summaries | Weekly |
| `agg_monthly_summary` | Monthly rollups | Monthly |

## Setup Instructions

### Prerequisites
- Google Cloud Project with BigQuery enabled
- Service account with BigQuery Admin role
- Supabase project with data

### 1. Create Dataset

```bash
# Set your project ID
export PROJECT_ID=your-project-id

# Create dataset
bq mk --dataset \
  --location=US \
  --description="LeadSniper Analytics Data Warehouse" \
  ${PROJECT_ID}:leadsniper_analytics
```

### 2. Create Tables

```bash
# Replace ${PROJECT_ID} in SQL files and run
cd bigquery/schemas

# Create fact tables
sed "s/\${PROJECT_ID}/${PROJECT_ID}/g" fact_tables.sql | bq query --use_legacy_sql=false

# Create dimension tables
sed "s/\${PROJECT_ID}/${PROJECT_ID}/g" dimension_tables.sql | bq query --use_legacy_sql=false

# Create aggregate tables
sed "s/\${PROJECT_ID}/${PROJECT_ID}/g" aggregate_tables.sql | bq query --use_legacy_sql=false

# Create views
sed "s/\${PROJECT_ID}/${PROJECT_ID}/g" ../views/analytics_views.sql | bq query --use_legacy_sql=false
```

### 3. Deploy ETL Pipeline

```bash
# Install dependencies
pip install google-cloud-bigquery supabase

# Set environment variables
export SUPABASE_URL=https://your-project.supabase.co
export SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
export GOOGLE_CLOUD_PROJECT=your-project-id
export BQ_DATASET=leadsniper_analytics

# Run ETL manually
cd bigquery/etl
python supabase_to_bigquery.py
```

### 4. Deploy as Cloud Function

```bash
# Deploy ETL function
gcloud functions deploy leadsniper-etl-daily \
  --runtime python311 \
  --trigger-topic leadsniper-etl-trigger \
  --entry-point run_daily_etl \
  --set-env-vars SUPABASE_URL=$SUPABASE_URL,SUPABASE_SERVICE_ROLE_KEY=$SUPABASE_SERVICE_ROLE_KEY,GOOGLE_CLOUD_PROJECT=$PROJECT_ID,BQ_DATASET=leadsniper_analytics \
  --memory 512MB \
  --timeout 540s

# Create Cloud Scheduler job (runs daily at 2 AM UTC)
gcloud scheduler jobs create pubsub leadsniper-etl-daily-trigger \
  --schedule="0 2 * * *" \
  --topic=leadsniper-etl-trigger \
  --message-body="{}"
```

## Available Views

### Dashboard Views
| View | Description |
|------|-------------|
| `v_daily_kpis` | Daily KPI metrics for dashboards |
| `v_search_summary` | Search activity overview |
| `v_lead_quality_distribution` | Lead quality breakdown |
| `v_weekly_trends` | Week-over-week trends |

### Analysis Views
| View | Description |
|------|-------------|
| `v_top_niches` | Most searched niches |
| `v_top_cities` | Most searched cities |
| `v_niche_leaderboard` | Niche performance ranking |
| `v_user_engagement` | User engagement metrics |

### Operations Views
| View | Description |
|------|-------------|
| `v_enrichment_performance` | API source performance |
| `v_content_generation_stats` | AI content statistics |
| `v_api_usage` | API usage and costs |
| `v_lead_funnel` | Lead funnel analysis |

### Campaign Views
| View | Description |
|------|-------------|
| `v_campaign_performance` | Campaign metrics |

## Sample Queries

### Daily Search Volume
```sql
SELECT * FROM `project.leadsniper_analytics.v_search_summary`
WHERE partition_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
ORDER BY partition_date DESC;
```

### Top Performing Niches
```sql
SELECT * FROM `project.leadsniper_analytics.v_niche_leaderboard`
LIMIT 10;
```

### User Engagement Analysis
```sql
SELECT
  engagement_status,
  COUNT(*) as users,
  AVG(total_searches) as avg_searches,
  AVG(total_leads) as avg_leads
FROM `project.leadsniper_analytics.v_user_engagement`
GROUP BY engagement_status;
```

### Week-over-Week Growth
```sql
SELECT * FROM `project.leadsniper_analytics.v_weekly_trends`
ORDER BY week_start DESC
LIMIT 8;
```

## Cost Optimization

### Partitioning
All fact tables are partitioned by `partition_date` to limit query scans.

### Clustering
Tables are clustered by frequently filtered columns:
- `fact_lead_searches`: niche, city
- `fact_lead_enrichments`: source, enrichment_type
- `fact_content_generations`: content_type, model_used

### Query Best Practices
1. Always filter on partition column (`partition_date`)
2. Use cluster columns in WHERE clauses
3. Prefer views over raw table scans
4. Use aggregate tables for dashboard queries

## Monitoring

### ETL Health Check
```sql
SELECT
  loaded_at,
  rows_processed,
  DATE_DIFF(CURRENT_TIMESTAMP(), loaded_at, HOUR) as hours_since_load
FROM `project.leadsniper_analytics.agg_daily_metrics`
ORDER BY loaded_at DESC
LIMIT 1;
```

### Data Freshness
```sql
SELECT
  'fact_lead_searches' as table_name,
  MAX(partition_date) as latest_partition,
  COUNT(*) as total_rows
FROM `project.leadsniper_analytics.fact_lead_searches`
UNION ALL
SELECT
  'fact_lead_enrichments',
  MAX(partition_date),
  COUNT(*)
FROM `project.leadsniper_analytics.fact_lead_enrichments`;
```

## Maintenance

### Purge Old Data (>2 years)
```sql
DELETE FROM `project.leadsniper_analytics.fact_lead_searches`
WHERE partition_date < DATE_SUB(CURRENT_DATE(), INTERVAL 730 DAY);
```

### Rebuild Aggregates
```bash
python supabase_to_bigquery.py full-refresh
```

---

*Version: 1.0*
*Last Updated: January 14, 2026*
