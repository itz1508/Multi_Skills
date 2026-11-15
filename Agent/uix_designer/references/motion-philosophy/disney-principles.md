# Disney's 12 Principles Adapted for UI

1. **Squash and Stretch** — Scale distortion on impact. Buttons squash to 0.96 on press, stretch to 1.04 on release. Keep area approximately constant.
2. **Anticipation** — Brief reverse motion before the main action. Card lifts 2px before sliding right. Tooltip shrinks 5% before expanding.
3. **Staging** — One focal point per moment. Dim other elements to 80% opacity when hero element enters. Only one major motion at a time.
4. **Straight Ahead vs Pose-to-Pose** — Use pose-to-pose (keyframe) for UI transitions. Use straight-ahead (per-frame) for particle effects and continuous motion.
5. **Follow-Through and Overlapping** — Elements don't stop simultaneously. Shadow arrives 50ms after card. Content fades 100ms after card lands. Settle with spring.
6. **Slow In and Slow Out** — Never linear for spatial movement. Decelerate into position (ease-out on entrance), accelerate away (ease-in on exit). Linear only for spinners and progress bars.
7. **Arcs** — Spatial motion follows gentle curves, not straight lines. 10px X offset at midpoint for card entrance. Vertical arcs for success pops.
8. **Secondary Action** — Supporting motion that reinforces the primary. Shadow shrinks during press. Icon shifts 2px. Ambient gradient pulses.
9. **Timing** — Match duration to element type. Tooltip 80-120ms, button 120-180ms, modal 300-400ms, page 400-600ms. See motion-personality.md.
10. **Exaggeration** — Push beyond realism for clarity. Scale pop to 1.08 instead of 1.02 for success states. Overshoot 15% for playful archetype.
11. **Solid Drawing** — 3D weight via shadow, depth, scale. Cards have consistent shadow elevation. Modals scale from 0.96 with shadow growth.
12. **Appeal** — Harmonious motion that feels good. Consistent personality. No jarring mismatches. Easing curves match the brand voice.

Source: re-written from LottieFiles/motion-design-skill research.
