# To Do List

n.b. This is for short quick notes of to give context about

- what is in progress
- what I want to do next

## Modify behavior of LeftPane buttons (Section, Channels)

User Story

- buttons act like a toggle/slider - user is selecting 'Section' behavior or 'channels' behavior
- select `section` -> click on section -> FeedPane is populated with articles from that section
- select `channels` -> click on section
  - FeedPane is clearned
  - LeftPane > `SectionView` view is replaced by `ChannelView`

Example:

- click on section "News" while in channel mode
  - SectionView is replaced by ChannelView
  - display a list of channels such as CNN, Fox News, BBC News, Vox...
  - user clicks on one of the channels -> the FeedPane is populated with just recent articles from that channel

### SectionView

- contains list of "sections" (either default sections or user-defined)

### ChannelView

- contains a list of all of the feed channels that are associated with a given section

### Tech Notes

- Create Pinia store (or use existing) to hold state of section/channel toggle
- Each section list item should have conditional behavior on @click based on value of section/channel state
  - if section/channel state == section:
    - click on section -> API call for section articles -> populate FeedPane with section articles
  - if section/channel state == channel:
    - click on section -> API call (?) for section's feedlist -> populate Pinia store (?)
      - replace SectionView with ChannelView (using section name as component title - (from Pinia store))
      - populate ChannelView with feedlist display names (from Pinia store)
      - user clicks on feedlist name -> API call for feed articles -> populate FeedPane with feed articles

#### Patterns

- toggle a view (replace/swap one view with another)
  - e.g. swap between SectionView and ChannelView
- populate Pinia store with state, retrieve state from Pinia store
  - e.g. Section name -> feedlist
- conditional click behavior
  - e.g. click on section - different behavior in section mode or channel mode
