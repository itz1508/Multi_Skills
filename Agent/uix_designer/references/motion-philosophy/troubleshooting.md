# Animation Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Looks robotic | Linear easing or no arcs | Add easing curves + arc paths |
| Feels too slow | Duration too long for element type | Check duration table, use ease-out |
| Feels cheap/flat | Missing secondary + ambient | Add shadow motion + background life |
| Too distracting | Too many elements moving | Apply 1/3 rule, reduce amplitude |
| No personality | Generic easing everywhere | Apply personality archetype consistently |
| Janky/stuttery | Animating layout properties | Use transform/opacity only, add will-change |
| Overshoot feels wrong | Mismatched archetype | Playful=10-20%, Premium=0%, Energetic=15-30% |
| Entrance feels heavy | Duration too long + no anticipation | Add 50ms anticipation, reduce duration 20% |
| Exit feels sluggish | Exit longer than entrance | Exit should be 60-70% of entrance duration |
| Stagger too slow | Total budget >500ms | Reduce per-item delay, cap at 40-60ms |

Source: re-written from LottieFiles/motion-design-skill research.
