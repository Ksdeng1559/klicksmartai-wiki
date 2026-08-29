BEGIN;


INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    'b1bc9d5e-394a-5396-9ef5-22299d956109'::uuid, '201ca3e4-35f5-4c89-b018-b3b7d964987c'::uuid,
    'Schedule kickoff call with Tak Ho + Zulliy Alnahas', 'Both principals have working emails (tak@gpcdevelopment.ca, zulliy@gpcdevelopment.ca) and phones. Propose 3 time slots in PT/ET overlap window. Address: Suite 2100-1177 W. Hastings Street, Vancouver, BC.', 'open', 'high',
    '2026-09-05T21:02:11.795261+00:00'::timestamptz, 'dennis',
    'organization', 'a4378ec5-2e50-5ac7-bf9c-c0e048fd5a84',
    '{"phase": "0-onboarding", "seed_source": "telegram/tak-ho-2026-04-16", "call_agenda_ref": "deliverables/seo/manifest.json"}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    '2ec1add2-48c8-5b79-9a8b-568e7d293a05'::uuid, '201ca3e4-35f5-4c89-b018-b3b7d964987c'::uuid,
    'Send engagement letter to GPC Development Ltd.', 'Engagement letter for SEO project per PROJECT_SETTINGS_2026-08-26. Reference site scope (audit + scoring), pricing per client-score report. Email to both principals.', 'open', 'high',
    '2026-09-03T21:02:11.795442+00:00'::timestamptz, 'dennis',
    'organization', 'a4378ec5-2e50-5ac7-bf9c-c0e048fd5a84',
    '{"phase": "0-onboarding", "reference": "deliverables/seo/CLIENT-SCORE-gpc-development-2026-08-28.html"}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    '56a5961e-5f39-5540-a834-53f2f5d9e551'::uuid, '201ca3e4-35f5-4c89-b018-b3b7d964987c'::uuid,
    'Verify GPC registered business address with Tak Ho', 'Source says Suite 2100-1177 W. Hastings Street, Vancouver, BC. Confirm via phone call (778-885-0633) before adding to legal/contract docs.', 'open', 'normal',
    '2026-09-08T21:02:11.795472+00:00'::timestamptz, 'dennis',
    NULL, NULL::uuid,
    '{"phase": "0-onboarding", "source": "telegram/tak-ho-2026-04-16"}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    'bc8d2c40-56ee-5160-9891-3de063be0069'::uuid, '201ca3e4-35f5-4c89-b018-b3b7d964987c'::uuid,
    'Import Tak Ho + Zulliy Alnahas LinkedIn profiles', 'Search LinkedIn for both co-founders. Add `linkedin_url` and any bio details to contacts table. Tag role=''Principal / Co-Founder'' already set.', 'open', 'low',
    '2026-09-12T21:02:11.795491+00:00'::timestamptz, 'dennis',
    NULL, NULL::uuid,
    '{"phase": "1-enrichment", "contacts": ["zulliy-alnahas", "tak-ho"]}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    'd4b86253-3d5b-5846-8daa-f8118ad7e98b'::uuid, '201ca3e4-35f5-4c89-b018-b3b7d964987c'::uuid,
    'Deliver initial SEO audit + client score report', 'Audit + scoring already produced 2026-08-26 + 2026-08-28. Schedule delivery walkthrough. Reference: deliverables/seo/audit-1page/audit/audit-quote-2026-08-26-gpc-development.html and deliverables/seo/CLIENT-SCORE-gpc-development-2026-08-28.html.', 'completed', 'high',
    '2026-08-22T21:02:11.795880+00:00'::timestamptz, 'dennis',
    NULL, NULL::uuid,
    '{"phase": "2-deliver", "delivered_via": "wiki + audit html"}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    '2a7e676e-7532-5978-a33e-2f29155c2532'::uuid, '201ca3e4-35f5-4c89-b018-b3b7d964987c'::uuid,
    'Mark gpc-development onboarding_status=''complete''', 'After engagement letter signed + kickoff call done, flip onboarding_status from ''pending'' → ''complete'' on public.workspaces row.', 'open', 'normal',
    '2026-09-28T21:02:11.795928+00:00'::timestamptz, 'dennis',
    NULL, NULL::uuid,
    '{"phase": "9-close"}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    '9cd11d6b-8263-50a4-b519-a3a49972b609'::uuid, '59fde87c-f305-4d4f-a2d9-1430759cbb1b'::uuid,
    'Schedule co-founder intro call with David Poole + Daniel Bailey', 'David Poole phone 816-405-6181 (verified 2026-08-10). Daniel Bailey — no phone yet. Propose 2 time slots for 30-min intro. Reg D 506(b) overlay applies (per IDENTITY.md).', 'open', 'high',
    '2026-09-05T21:02:11.795975+00:00'::timestamptz, 'dennis',
    'organization', '20248ed2-7fd0-53df-997c-e02e98878adf',
    '{"phase": "0-onboarding", "reg_d_overlay": "506(b)"}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    '87cc7995-f836-51c7-85a5-94d7d3e636cb'::uuid, '59fde87c-f305-4d4f-a2d9-1430759cbb1b'::uuid,
    'Confirm Daniel Bailey phone number', 'Daniel Bailey phone is currently NULL in contacts table. Email or DM to request.', 'open', 'normal',
    '2026-09-12T21:02:11.796011+00:00'::timestamptz, 'dennis',
    'contact', '8e0e727d-c006-5c99-a3de-df72d643097f',
    '{"phase": "0-onboarding", "missing_field": "phone"}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    '09ce7368-c3a8-5f02-acb9-19ab1a3adffb'::uuid, '59fde87c-f305-4d4f-a2d9-1430759cbb1b'::uuid,
    'Schedule intro call with Polsinelli PC family-office counsel', 'Primary contact: Gregory M. Kratofil Jr., KC Office Managing Partner, 816-360-4363. Reference IDENTITY.md Reg D 506(b) overlay. Goal: verify counsel sign-off + introduce KlickSmartAI''s role.', 'open', 'high',
    '2026-09-12T21:02:11.796032+00:00'::timestamptz, 'dennis',
    'organization', '5454ddf2-9783-541e-aa62-a077c66cc874',
    '{"phase": "0-onboarding", "source": "drafts/kc-family-office-law-firm-channel-2026-08-22.md"}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    '4f4bc087-3753-5723-9392-6d6d5185f26b'::uuid, '59fde87c-f305-4d4f-a2d9-1430759cbb1b'::uuid,
    'Review 20-name co-sponsor GP target list (Tier 1 vs Tier 2/3)', 'Source: projects/co-sponsor-gp-target-list.md. Tier 1 (5 names) sourced + verified. Tier 2/3 (15 names) flagged NEEDS RESEARCH. Decide: do we kick off enrichment on Tier 2/3 now, or wait for Dennis approval?', 'open', 'high',
    '2026-09-03T21:02:11.796050+00:00'::timestamptz, 'dennis',
    NULL, NULL::uuid,
    '{"phase": "1-enrichment", "tier_1_count": 5, "tier_2_count": 15, "source_flag": "NEEDS RESEARCH"}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    '925d0587-abf1-5b8a-9c0b-e05b29f4269c'::uuid, '59fde87c-f305-4d4f-a2d9-1430759cbb1b'::uuid,
    'Verify Tier 1 GP contacts (Ewing Marion Kauffman, Hall, Bloch, Menorah, Health Forward)', 'Tier 1 entries in co-sponsor-gp-target-list.md need email + LinkedIn enrichment. Source file flags these as ''verified organization'' but not ''verified contact''. Do not outreach until enriched.', 'open', 'high',
    '2026-09-19T21:02:11.796068+00:00'::timestamptz, 'dennis',
    NULL, NULL::uuid,
    '{"phase": "1-enrichment", "tier_1_orgs": ["Ewing Marion Kauffman Foundation", "Hall Family Foundation", "Bloch Family Foundation", "Menorah Heritage Foundation", "Health Forward Foundation"]}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    '98a1db7b-6d47-5a41-9f3f-787a78514371'::uuid, '59fde87c-f305-4d4f-a2d9-1430759cbb1b'::uuid,
    'LinkedIn enrichment for internal Veritas team', 'Daniel Bailey + Mike Poole have NULL LinkedIn URLs. David Poole''s already linked per IDENTITY.md signer block.', 'open', 'low',
    '2026-09-19T21:02:11.796085+00:00'::timestamptz, 'dennis',
    NULL, NULL::uuid,
    '{"phase": "1-enrichment", "contacts": ["daniel-bailey", "mike-poole"]}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    'eca49342-8dee-5108-902c-63dce16b7f8b'::uuid, '59fde87c-f305-4d4f-a2d9-1430759cbb1b'::uuid,
    'Deliver Polsinelli + Lathrop GPM outreach channel strategy', 'Source doc: drafts/kc-family-office-law-firm-channel-2026-08-22.md. Strategy already drafted. Schedule review with Dennis + 7-touch outreach playbook alignment.', 'open', 'normal',
    '2026-09-08T21:02:11.796103+00:00'::timestamptz, 'dennis',
    NULL, NULL::uuid,
    '{"phase": "2-deliver", "source": "drafts/kc-family-office-law-firm-channel-2026-08-22.md"}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;

INSERT INTO public.tasks (
    id, workspace_id, title, description, status, priority,
    due_at, assigned_to, related_entity_type, related_entity_id,
    metadata
) VALUES (
    '3f7bcdb1-0e43-5297-8c56-7b92cd896a2c'::uuid, '59fde87c-f305-4d4f-a2d9-1430759cbb1b'::uuid,
    'Mark veritas-developments onboarding_status=''complete''', 'After kickoff call + co-sponsor strategy aligned, flip onboarding_status from ''pending'' → ''complete'' on public.workspaces row.', 'open', 'normal',
    '2026-10-13T21:02:11.796119+00:00'::timestamptz, 'dennis',
    NULL, NULL::uuid,
    '{"phase": "9-close"}'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title = EXCLUDED.title,
    description = EXCLUDED.description,
    status = EXCLUDED.status,
    priority = EXCLUDED.priority,
    due_at = EXCLUDED.due_at,
    assigned_to = EXCLUDED.assigned_to,
    related_entity_type = EXCLUDED.related_entity_type,
    related_entity_id = EXCLUDED.related_entity_id,
    metadata = EXCLUDED.metadata;


COMMIT;
